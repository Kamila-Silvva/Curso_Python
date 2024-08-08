dias = {
    1: 'Segunda-feira',
    2: 'Terça-feira',
    3: 'Quarta-feira',
    4: 'Quinta-feira',
    5: 'Sexta-feira',
    6: 'Sábado',
    7: 'Domingo'
}

numero = int(input('Digite um número de 1 á 7: '))

if numero in dias: #número em dias
    print(dias[numero]) #dias chama o nome do dia da semana e número se refere ao dias
else:
    print('Este dia e inválido!!')



