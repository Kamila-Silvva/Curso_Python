"""
> - Esquerda 
< - Direita
^ - centro
= - força o numero a aparecer antes dos zeros
Sinal - + ou -
Ex: 0>-100,1f
Conversion flags - !r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{900000000000:0=+,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')