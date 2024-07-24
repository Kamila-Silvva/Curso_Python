Nome = 'Kamila Silva'
Idade = 20
Peso = 88
Altura = 1.63 
IMC = Peso / (Altura * Altura)

print('Nome:', Nome)
print('Idade', Idade)
print('Altura:', Altura, 'de altura')
print(f'Seu IMC é: {IMC:.2f}')

# formatação de strings == {altura:.2f} para colocar em reais e somente utilizar uma virgular do seguinte modo: {Valor:,.f}
# nunca se esquecer que para que a formatação aconteça e necessário colocar o f no início antes das aspas simples

# name = 'nome: {}'
# formato = name.format(Nome)

# print(formato)

nome = "Luiz"
idade = 23
formato = f'{nome} tem {idade:.2f} anos'
print(10 * 20)
