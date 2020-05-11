""" Crie um programa que leia NOME, SEXO e IDADE de vária pessoas, guardando os dados de cada pessoa em um dicionário e
todos os dicionarios em um lista. No final, mostre:
A) quantas pessoas foram cadastradas
B) A Media de idade do grupo
C) uma lista com todas as mulheres.
D) Uma lista com todas as pessoas com idade acima da média """

pessoa = dict()
todos = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: (M ou F): ')).upper()[0]

        if pessoa['sexo'] in "MF":
            break
        print('SEXO INVALIDO! digite apenas M ou F')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    todos.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar: [S/N]: ')).upper()[0]
        if resp in "SN":
            break
        print("ERRO! responda apenas com S ou N")
    if resp == 'N':
        break

print('-='*30)
print(f'A) Ao todo temos {len(todos)} pessoas cadastradas')
media = soma / len(todos)
print(f'B) A media de idade é de {media:5.2f} anos')
print('C) As mulher cadastradas foram ', end='')
for p in todos:
    if p['sexo'] in 'F':
        print(f'{p["nome"]}', end=' ')
print()
print('D) lista das pessoas que estao acimda da média: ', end='')
for p in todos:
    if p['idade'] >= media:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v}')
        print()
print('<<< ENCERRADO >>>')
