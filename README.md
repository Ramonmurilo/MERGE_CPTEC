<h1 align="center">Como utilizar: </h1>

<h3>Configuração do ambiente: </h3>
<p>

Clone este repositório git para a sua máquina com o comando:
  
```
git clone https://github.com/Ramonmurilo/MERGE_CPTEC.git
```

Reproduza o ambiente a partir do arquivo environment.yaml
```
conda env create -n nome_qualquer -f environment.yaml
```
 </p>


<h3>Crie seu script python</h3>
<p>

Importe o módulo com as rotinas (obs.:este exxemplo funciona caso o arquivo .py e o módulo estejam no mesmo diretório)
```
import cptec_merge
```

Exemplos de comandos e usos:

# Baixando dados horarios do dia atual
# Serão salvos na mesma pasta do script
# baixa dados até a hora atual. Se já houver dados prévios, serão sobrescritos
```
cptec_merge.baixar_dados(discretizacao='hora',hoje=True)
```
# Baixando dados horarios de um dia específico
# Serão salvos na pasta teste
```
cptec_merge.baixar_dados(discretizacao='hora',data_string='21-07-2021', diretorio_saida='teste')
```

# Baixando dado diario do dia atual
# Serão salvos na mesma pasta do script
```
cptec_merge.baixar_dados(discretizacao='diario',hoje=True)
```

# Baixando dado diario de um dia específico
# Serão salvos na pasta teste
```
cptec_merge.baixar_dados(discretizacao='diario',data_string='21-07-2021', diretorio_saida='teste')
```
 </p>