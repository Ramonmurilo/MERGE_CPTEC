import cptec_merge


'''
é necessário ter a biblioteca "pendulum" e "requests" instaladas em seu ambiente

'''

# Baixando dados horarios do dia atual
# Serão salvos na mesma pasta do script
# baixa dados até a hora atual. Se já houver dados prévios, serão sobrescritos
cptec_merge.baixar_dados(discretizacao='hora',hoje=True)

# Baixando dados horarios de um dia específico
# Serão salvos na pasta teste
cptec_merge.baixar_dados(discretizacao='hora',data_string='21-07-2021', diretorio_saida='teste')


# Baixando dado diario do dia atual
# Serão salvos na mesma pasta do script
cptec_merge.baixar_dados(discretizacao='diario',hoje=True)

# Baixando dado diario de um dia específico
# Serão salvos na pasta do script
cptec_merge.baixar_dados(discretizacao='diario',data_string='21-07-2021', diretorio_saida='teste')
