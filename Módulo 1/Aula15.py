#Operadires in e not in

"""nome = 'Kamila'

print('K' in nome)
print('m' in nome) # está no
print(10 * '-')
print('K' not in nome) #não está
print('m' not in nome)"""

nome = input('Digite o seu nome: ')
encontrar = input('O que deseja encontrar? ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')