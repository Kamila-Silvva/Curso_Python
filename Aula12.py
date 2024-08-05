"""
Operadores lógicos

and =  e
or = ou
not = não
and = Todas as condições precisam ser verdadeiras
Se qualquer valor for considerado falso, a expressão inteira será avaliada naqeuele valor
São considerados *falsy* == 0 0.0 '' False
None = usado para representar um não valor 
"""

entrada = input('[E]ntrar [S]air: ')
senhaDigitada = input('Senha: ')

senhaPermitda = 'Ksk2209*'

if entrada == 'E' and senhaDigitada == senhaPermitda:
    print('Entrar')
else:
    print('Sair')