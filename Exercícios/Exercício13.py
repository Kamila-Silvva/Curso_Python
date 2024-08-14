#Solicita informações do vendedor
nome_vendedor = input('Qual o nome do vendedor? ')
vendas_vendedor = float(input('Qual o total de vendas do mês? '))

#Determinar o perfil e a porcetagem da comissão
if vendas_vendedor > 50000:
    perfil = 'Vendedor Sênior'
    comissao = 10
elif (30000 <= vendas_vendedor <= 50000):
    perfil = 'Vendedor Pleno'
    comissao = 7
else:
    perfil = 'Vendedor Junior'
    comissao = 5

#Imprime o perfil e o valor das vendas
print(f'Perfil: {perfil}')
print(f'Valor total das vendas do mês: R$ {vendas_vendedor:.2f}')

#Calculo da comissão
calculo_comissao = vendas_vendedor * comissao / 100

#Imprime o resultado da comissão
print(f'Comissão a ser recebida: R$ {calculo_comissao:.2f}')

