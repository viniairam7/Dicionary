aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}:  '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado!'
elif 5 <= aluno['Média'] < 7:
    aluno['Situação'] = 'Reprovado.'
else:
    aluno['Situação'] = 'Reprovado.'
print('/'*30)
for k, v in aluno.items():
    print(f'{k}: {v}.')
