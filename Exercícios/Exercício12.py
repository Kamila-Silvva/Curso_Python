# Entrada de dados
gastos_mensal = float(input('Qual o valor gasto mensalmente na loja? '))
tempo_cliente = int(input('Há quanto tempo é cliente da loja? '))

# Determinação do perfil do cliente
if gastos_mensal > 2000 and tempo_cliente > 5:
    pontos_por_real = 10
    perfil = 'Cliente VIP'
elif (1000 <= gastos_mensal <= 2000) or tempo_cliente >= 3:
    pontos_por_real = 5
    perfil = 'Cliente Regular'
else:
    pontos_por_real = 2
    perfil = 'Cliente Novo'

# Resultado do perfil e pontos por real gasto
print(f'Perfil: {perfil}')
print(f'Pontos por real gasto: {pontos_por_real}')

# Cálculo dos pontos acumulados
valor_gasto = float(input('Qual foi o valor gasto na loja nesta compra? '))
pontos_gerados = valor_gasto * pontos_por_real

# Adicionando os pontos acumulados anteriormente
pontos_acumulados = float(input('Digite os pontos acumulados anteriormente (se houver): '))
total_de_pontos = pontos_gerados + pontos_acumulados

# Exibindo o total de pontos
print(f'Total de pontos acumulados: {total_de_pontos:.2f}')
