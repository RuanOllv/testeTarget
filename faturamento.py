import json

# Leitura dos dados do arquivo JSON
with open('dados.json') as f:
    faturamento = json.load(f)

# Inicialização das variáveis para cálculo do menor, maior e média
menor = faturamento[0]['valor']
maior = faturamento[0]['valor']
soma = 0
dias_com_faturamento_acima_da_media = 0

# Cálculo da soma e contagem dos dias com faturamento acima da média
for dia in faturamento:
    if dia['valor'] < menor:
        menor = dia['valor']
    if dia['valor'] > maior:
        maior = dia['valor']
    if dia['valor'] > 0:
        soma += dia['valor']

media = soma / len([dia for dia in faturamento if dia['valor'] > 0])

for dia in faturamento:
    if dia['valor'] > media:
        dias_com_faturamento_acima_da_media += 1

# Impressão dos resultados
print(f"Menor valor de faturamento: R$ {menor:.2f}")
print(f"Maior valor de faturamento: R$ {maior:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_com_faturamento_acima_da_media}")
