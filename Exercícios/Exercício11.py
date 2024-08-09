gastos_mensal = float(input('Qual o valor gasto mensalmente na loja? '))
tempo_cliente = int(input('Há quanto tempo é cliente da loja (em anos)? '))

if gastos_mensal > 100 and tempo_cliente > 5:
    desconto = 20
    perfil = 'Cliente Vip'
elif (500 <= gastos_mensal <= 100) or tempo_cliente >= 3:
    desconto = 10
    perfil = 'Cliente Regular'
else:
    desconto = 0
    perfil = 'Cliente novo'
    
print(f'Perfil: {perfil}')
print(f'Desconoto: {desconto}%')

valor_produto = float(input('Qual o valor do produto: '))

valor_com_desconto = valor_produto - (valor_produto * desconto / 100)

print(f'O valor do produto com desconto é: R$ {valor_com_desconto:.2f}')