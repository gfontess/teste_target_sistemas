import json

# Lendo os dados de faturamento mensal de um arquivo JSON
with open('teste_target_sistemas/faturamento.json', 'r') as file:
    faturamento_mensal = json.load(file)

# Criando uma lista com os valores de faturamento de cada dia do mês
valores_diarios = [dicionario['valor'] for dicionario in faturamento_mensal]

# Calculando o menor e o maior valor de faturamento ocorrido em um dia do mês
menor_faturamento = min(valores_diarios)
maior_faturamento = max(valores_diarios)

# Calculando a média mensal de faturamento, excluindo os dias sem faturamento
dias_com_faturamento = [valor for valor in valores_diarios if valor > 0]
media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)

# Contando o número de dias no mês em que o valor de faturamento diário foi superior à média mensal
dias_acima_da_media = len([valor for valor in valores_diarios if valor > media_mensal])

# Imprimindo os resultados
print('Menor valor de faturamento: R$ {:.2f}'.format(menor_faturamento))
print('Maior valor de faturamento: R$ {:.2f}'.format(maior_faturamento))
print('Numero de dias com faturamento acima da media: {}'.format(dias_acima_da_media))
