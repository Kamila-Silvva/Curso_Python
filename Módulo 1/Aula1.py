"""
DocString 
No python ultilizamos as aspas triplhas duas vezes, para abertura e fechamento para comentários grandes, não e ultilizado as barras como nas outras linguagens
"""
'''
Pode ser ultizado aspas simples também
'''

# no python para comentar o código usamos o jogo da velha. 
print(1 + 45) 

print(2 / 10)
print(10 / 2)
print('Os resultados')

print(12 + 89, 78, sep="-") #sep= e usado para solicitar um novo separador
print(12 + 78, sep="-") #sep= e usado para solicitar um novo separador
print(12, 78, sep="-") #sep= e usado para solicitar um novo separador
print(12, 89, 78, sep="-") #sep= e usado para solicitar um novo separador

print("Kamila \"kamila\"") #Caracter de escape sere imprimido em aspas o que está antes da \ e com aspa o que esta dentro da \\

print(r"Kamila \"kamila\"") #faz a mesma coisa da \ acima porém imprimindo junto as \ do escape

#uma forma mais simples de fazer o escape e iniciando o print com aspas simples e fazendo o escape dentro dele com aspas duplas, assim o código ficará limpo e terá o mesmo resultado
print('Kamila "kamila"')

# Ei!
print('Python')

print('Explicito', 'é', 'melhor-que-implicito.', sep='-') 
print('Simples', 'e', 'melhor-que-complexo.', sep='-')

print('Explícito', 'é', 'melhor " do que implícito')