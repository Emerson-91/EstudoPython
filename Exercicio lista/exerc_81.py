""" Crie um programa que vai ler varios numeros e colocar em uma lista. Depois disso, mostre:
A) Quantos numeros foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e esta ou nao na lista """

lista = []
while True:
    n = int(input("Digite um valor: "))
    lista.append(n)
    r = str(input("Quer continuar[S/N]: ")).upper()[0]
    if r in "N":
        break
lista.sort(reverse=True)
print(f"Foram digitados {len(lista)} numeros")
print(f'lista em ordem decrescente: {lista}')
if 5 in lista:
    print("O numero 5 esta contido na lista!!")
else:
    print("O numero 5 nao esta na lista!! ")

