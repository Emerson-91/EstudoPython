""" Faca um programa que leia nome e peso de varias pessoas, guardando tudo e uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) uma listagem com as pessoas mais leves
"""

pessoa = list()
dado = list()
maior = menor = 0
while True:
    dado.append(str(input('Digite o nome: ')))
    dado.append(float(input('Digite o peso: ')))
    if len(pessoa) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    pessoa.append(dado[:])
    dado.clear()
    r = str(input("Quer Continuar? [S/N]")).upper()[0]
    if r in 'N':
        break
print(f'Ao todo foram {len(pessoa)} pessoas cadastradas.')
print(f'O maior peso foi de {maior} KG. O maior peso foi de ', end='')
for p in pessoa:
    if p[1] == maior:
        print(f' {p[0]}', end='')
print()
print(f'O menor peso foi de {menor}KG. O menor peso foi de ', end='')
for p in pessoa:
    if p[1] == menor:
        print(f' {p[0]}', end='')

