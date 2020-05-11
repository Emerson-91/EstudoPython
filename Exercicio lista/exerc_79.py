""" Crie um programa onde o usuario possa digitar varios valores numericos e cadastre-os em uma lista. Caso o numero já
exista la dentro, ele nao sera adicionado. No final, serao exibidos todos os valores unicos digitados, em ordem crescente"""

lista = []
while True:
    n = int(input('Informe um valor: '))
    if n not in lista:
        lista.append(n)
    elif n in lista:
        print("Numero ja cadastrado! ")
    r = str(input("Que continuar? [S/N]: ")).upper()[0]
    if r in 'N':
        break
    elif r not in 'NS':
        print("Dados incorretos! informe S ou N")
lista.sort()
print(f'Numeros cadastrados em ordem crescente: {lista} ')

