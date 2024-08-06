nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))
nota3 = int(input('Digite a terceira nota: '))

somaNotas = nota1 + nota2 + nota3

media = somaNotas // 3

print(f'A sua média final é: {media:.2f}')

if media >= 7:
    print('Aprovado!!')
elif 6 <= media < 7:
    print('Possibilidade de recuperação!')
else: 
    print('Reprovado!')

