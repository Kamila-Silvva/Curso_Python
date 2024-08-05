"""
Operadores relacionais (de comparação)
> maior que 
>= maior ou igual
< menor que
<= menor ou igual
== igual
!= diferente
"""

numberOne = int(input("Digite o primeiro número: "))
numeberTwo = int(input("Digite o sengundo número: "))

if numberOne >= numeberTwo:
    print(numberOne, 'maior que', numeberTwo)
elif numberOne <= numeberTwo:
    print(numberOne, "menor que", numeberTwo)
if numberOne == numeberTwo:
    print(numberOne, "igual a ", numeberTwo)
elif numberOne != numeberTwo:
    print(numberOne, "diferente de", numeberTwo)
else:
    print("Operação inválida")

