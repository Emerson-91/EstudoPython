""" Faca um programa que leia nome e media de um aluno, guardando tambem a situacao em um dicionario.
no final, mostre o coeudo da estrutura na tela"""

aluno = dict()

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
print(f'Nome é igual a {aluno["nome"]}')
print(f'Media é igual a {aluno["media"]}')
if aluno['media'] <= 6.0:
    print('A situacao é reprovado')
elif aluno['media'] > 6.0:
    print('A situacao é APROVADO')

