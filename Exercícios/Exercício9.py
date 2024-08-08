nome_do_produto = input('Informe o nome do produto: ')
unidades_disponiveis_estoque = int(input('informe a quantidade de unidades dispóniveis no estoque: '))
valor_unitario = float(input('Valor unitário do produto: '))
valorMaximo = int(input('Qual o valor máximo do produto: '))

if unidades_disponiveis_estoque >= 1:
    print('O produto se encontra disponível no estoque!')
else:
    print('O produto não se encontra disponível no estoque!')

valor_total = unidades_disponiveis_estoque * valor_unitario

if valor_total <= valorMaximo:
    print('O valor está dentro dos limites estabelecidos!')
else:
    print('O valor está acima do limite estabelecido!')

print(f'Valor total do estoque: R$ {valor_total:.2f}')