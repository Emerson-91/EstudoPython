""" Crie um programa onde o usuario possa digitar sete valores numericos e cadastre-os em uma lisa unicaque mantenha
separados os valores pares e impares. No final, mostre os valores ares e impares em ordem crescente """

n = [[],[]]

for c in range(0,7):
    num = int(input(f'Digite o {c+1} valor: '))
    res = num % 2
    if res == 0:
        n[0].append(num)
    else:
        n[1].append(num)
n[0].sort()
n[1].sort()
print(f'Numeros pares: {n[0]}')
print(f'Numeros impares {n[1]}')