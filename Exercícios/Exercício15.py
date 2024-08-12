infoSalario = float(input('Qual o salário mnensal: '))

if infoSalario <= 2000:
    faixa = 'insento'
elif (2000.01 <= infoSalario <= 3500):
    faixa = 'faixa 1'
    calculoImposto = (infoSalario - 2000) * (8 / 100)
elif (3500.01 <= infoSalario <= 5000):
    faixa = 'faixa 2'
    calculoImposto = (1500 * 8 / 100) + (infoSalario - 3500) * (18 / 100)
else:
    faixa = 'faixa 3'
    calculoImposto = (1500 * 8 / 100) + (1500 * 18 / 100) + (infoSalario - 5000) * (27 / 100)

print(f'Faixa: {faixa}')
print(f'Total de imposto a pagar: R${calculoImposto:.2f}')


    
