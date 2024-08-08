# Coleta de dados do usuário
titular_nome = input('Informe o nome do titular: ')
titular_idade = int(input('Idade do titular: '))

# Verificação da idade
Idade_minima = 21
Idade_limite = 65

if Idade_minima <= titular_idade <= Idade_limite:
    print('Idade dentro dos limites permitidos!')
else:
    print('Idade fora dos limites permitidos! Não é possível solicitar o empréstimo.')

# Verificação da renda
titular_renda = float(input('Renda mensal do titular: '))
renda_minima = 3000.00

if titular_renda >= renda_minima:
    print('Renda apta para solicitar empréstimo.')
else:
    print('Renda insuficiente para solicitar o empréstimo.')

# Verificação da experiência de trabalho
titular_experiencia = int(input('Anos de experiência de trabalho: '))
experiencia_minima = 2

if titular_experiencia >= experiencia_minima:
    print('Tempo de experiência apto para solicitar empréstimo.')
else:
    print('Tempo de experiência insuficiente para solicitar o empréstimo.')

# Verificação de restrições no CPF
titular_restricoes = input('Tem restrições no CPF? (Responda com [Sim] ou [Não]): ')

if titular_restricoes == 'Não':
    print('Titular sem restrições no CPF.')
else:
    print('Titular com restrições no CPF. Não é apto para solicitar o empréstimo!')
