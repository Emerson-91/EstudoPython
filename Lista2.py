teste = []
teste.append('Emerson')
teste.append('28')
print(teste)
galera = list()
# COLOCAR [:] PARA COPIAR UMA LISTA PARA OUTRA
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = '25'
galera.append(teste[:])
print(galera)
print("=-"*30)
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')
print("=-"*30)
galera2 = list()
dado = list()
totmai = totmen = 0
for c in range(0,3):
    dado.append(str(input("Digite o nome: ")))
    dado.append(int(input("Digite a idade: ")))
    galera2.append(dado[:])
    dado.clear()
for p in galera2:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade. ')
        totmai += 1
    else:
        print((f'{p[0]} é menor de idade'))
        totmen += 1
print(f'Temos {totmai} maiores de idade e {totmen} menores de idade.')
