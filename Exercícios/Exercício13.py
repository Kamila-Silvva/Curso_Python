nome_vendedor = input('Qual o nome do vendedor? ')
vendas_vendedor = float(input('Qual o total de vendas do mês? '))

if vendas_vendedor > 50000:
    perfil = 'Vendedor Sênior'
    comissao = 10
elif (30000 <= vendas_vendedor <= 50000):
    perfil = 'Vendedor Pleno'
    comissao = 7
else:
    perfil = 'Vendedor Junior'
    comissao = 5
    
print(f'Perfil: {perfil}')
print(f'Valor total das vendas do mês: R$ {vendas_vendedor:.2f}')

calculo_comissao = vendas_vendedor * comissao / 100

print(f'Comissão a ser recebida: R$ {calculo_comissao:.2f}')

