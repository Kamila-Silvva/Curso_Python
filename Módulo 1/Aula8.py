#Input e utilizado para solicitar dados para o usuário

#função

# data_de_nascimento = input('Insira a data de nascimento: ') #dessa forma o input ler somente as strings
# ano_atual = input('Insira a data atual: ')

# print(f'A sua idade é: {data_de_nascimento - ano_atual}')

# numero1 = int(input('Digite um número: ')) #não e muito prudente fazer a soma desta forma
# numero2 = int(input('Digite outro número: '))

# print(f'A soma dos números é: {numero1 + numero2}')

# A forma mais prudente de fazer a soma será por meio da checagem 

numero1 = input('Digite um número: ')
numero2 = input('Digite outro número: ')

#checagem

int_numero1 = int(numero1)
int_numero2 = int(numero2)

print(f'A soma dos números é: {numero1 + numero2}')