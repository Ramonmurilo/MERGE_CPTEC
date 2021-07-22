import requests
from pathlib import Path
import pendulum
import sys
import os

def baixar_dados(discretizacao='diario',data_string=None, hoje=False, diretorio_saida=os.getcwd()):
  """
    
  Baixa os dados merge do CPTEC em descritização horária ou diária.
  
  Args:
      discretizacao (str): recebe a descritização desejada. Recebe 'diario' ou 'horario'
      data_string (str): recebe a data requerida em formato string 'DD-MM-YYYY'
      hoje (bool): habilita o uso da data atual. Sobrescreve a data_string
      diretorio_saida (str): caminho onde deseja salvar os arquivos
  |
  Returns:
      str: nome do arquivo baixado
  |
  |
  """

  data_requerida = pendulum.now('America/Sao_Paulo') if hoje else pendulum.from_format(data_string, 'DD-MM-YYYY')
  
  # tratativa de erro para o nome da discretização
  discretizacao = discretizacao.lower()
  diario = ['diario','diário','diaria','daily','dia']
  horario =['horário','horario','horária','horaria','hora','horas']


  if discretizacao in diario:

    url_base = 'http://ftp.cptec.inpe.br/modelos/tempo/MERGE/GPM/DAILY'
    arquivo = f'MERGE_CPTEC_{data_requerida.format("YYYYMMDD")}.grib2'
    url=f'{url_base}/{data_requerida.format("YYYY/MM")}/{arquivo}'

    resp=requests.get(url)

    if resp.status_code == 200:

      resp=requests.get(url).content
      diretorio = Path(diretorio_saida, arquivo)

      with open(diretorio, "wb") as arquivo_:
        arquivo_.write(resp)
      print(f"{arquivo} [ok]")

    elif resp.status_code == 404:

      sys.exit('Erro 404. Arquivo ainda não disponível')


  elif discretizacao in horario:

    range_de_horas_do_dia_escolhido = range(0,int(data_requerida.format('HH'))) if hoje else range(0,24)

    for hora in range_de_horas_do_dia_escolhido:

      hora_corrigida = hora if hora >= 10 else '0'+str(hora)
      url_base = f'http://ftp.cptec.inpe.br/modelos/tempo/MERGE/GPM/HOURLY/{data_requerida.format("YYYY/MM/DD")}'
      arquivo = f'MERGE_CPTEC_{data_requerida.format("YYYYMMDD")}{hora_corrigida}.grib2'
      url=f'{url_base}/{arquivo}'
      
      resp=requests.get(url).content
      diretorio = Path(diretorio_saida, arquivo)

      with open(diretorio, "wb") as arquivo_:
        arquivo_.write(resp)
        print(f"{arquivo} [ok]")

  return arquivo