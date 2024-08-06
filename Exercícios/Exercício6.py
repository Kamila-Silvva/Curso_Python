numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))

if numero1 > 0 and numero2 > 0:
    if (numero1 + numero2) > 10:
        print('Ambos os números são positivos e a soma deles é maior que 10.')
    else:
        print('Ambos os números são positivos, mas a soma deles não é maior que 10.')
else:
    print('Pelo menos um dos número e positivo')