""" Crie um programa que vai ler varios numeros e colocar em uma lista. Depois disso, mostre:
A) Quantos numeros foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e esta ou nao na lista """

lista = []
#for c in len(lista):
n = int(input("Digite um valor: "))
lista.append(n)
r = str(input("Quer continuar[S/N]: ")).upper()[0]
    while r in "N":
        break
