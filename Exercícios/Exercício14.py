funcionario_nome = input('Nome do funcionário: ')
funcionario_salário = float(input('Salário anual: '))
funcionario_tempo_de_servicos = int(input('Tempo de serviço em anos: '))

if funcionario_tempo_de_servicos > 10:
    bonus = 15
elif (5 <= funcionario_tempo_de_servicos <= 10):
    bonus = 10
else: 
    bonus = 5

print(f'{funcionario_nome}trabalha na empresa a {funcionario_tempo_de_servicos} anos')
print(f'{funcionario_nome}irá receber {bonus} de bônus')

total_bonus = funcionario_salário * bonus / 100

print(f'O bônus anual será de: R$ {total_bonus:.2f}')