""" Crie um programa que vai ler varios numeros e colocar em uma lista.
 Depois disso, crie duas listas extras que vao contar apenas os valores pares e os valores impares digitados, respectivamente
 Ao final, mostre o conteudo das tres listas geradas.
 """

lista = []
par = []
impar=[]
while True:
    n = int(input("Digite um valor: "))
    lista.append(n)
    r = n %2
    resp = str(input("Quer continuar [S/N]: ")).upper()[0]
    if r == 0:
        par.append(n)
    else:
        impar.append(n)
    if resp in "N":
        break
print(f'Lista completa: {lista}')
print(f'Somente numeros pares: {par}')
print(f'Somente numeros impares {impar}')
