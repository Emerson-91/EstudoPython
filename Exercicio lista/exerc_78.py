""" Faca um programa que leia 5 VALORES e guarde-os em uma listta
No final mostre qual foi o maior e o menor valor digitado e as suas respectivas posicoes na lista"""

lista = []
maior = []
menor = []
for c in range(0,5):
    lista.append(int(input(f"informe o valor {c}: ")))
for posicao, valores in enumerate(lista):
    if valores == max(lista):
        maior.append(posicao)
    elif valores ==min(lista):
        menor.append(posicao)
print(f"Voce digitou os valores: {lista}")
print(f"O menor valor é {min(lista)} nas posicoes {menor}")
print(f"O MAIOR valor é {max(lista)} nas posicoes {maior}")

