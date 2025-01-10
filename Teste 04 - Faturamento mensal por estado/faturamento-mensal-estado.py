#4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
#• SP – R$67.836,43
#• RJ – R$36.678,66
#• MG – R$29.229,88
#• ES – R$27.165,48
#• Outros – R$19.849,53

#Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.  

#Dados dos faturamentos por estado
faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

faturamento_total = sum(faturamento.values())

#Cálculo do percentual de cada estado
percentuais = {}
for estado, valor in faturamento.items():
    percentual = (valor / faturamento_total) * 100
    percentuais[estado] = percentual

print("Percentual de Representação por Estado no Faturamento Mensal:")
print("-" * 60)
print(f"{'Estado':<10}{'Faturamento (R$)':<20}{'Percentual (%)':<20}")
print("-" * 60)

for estado, percentual in percentuais.items():
    valor = faturamento[estado]
    print(f"{estado:<10}{valor:<20,.2f}{percentual:<20.2f}")

print("-" * 60)
print(f"{'Total':<10}{faturamento_total:<20,.2f}{'100.00':<20}")
