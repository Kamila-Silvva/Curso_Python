primeiroValor = int(input('Digite o primeiro valor: '))
segundoValor = int(input('Digite o segundo valor: '))

if primeiroValor >= segundoValor:
    print(primeiroValor, 'maior que', segundoValor)
elif primeiroValor <= segundoValor:
    print(primeiroValor, 'menor que', segundoValor)
if primeiroValor == segundoValor:
    print(primeiroValor, 'igual', segundoValor)
elif primeiroValor != segundoValor:
    print(primeiroValor, 'diferete de', segundoValor)
else:
    print('Operação inválida!!')