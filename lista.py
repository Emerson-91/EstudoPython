lista= ['hamburguer', 'suco', 'pizza', 'picole']
def teste():
    print()
    print(lista)
    print()
    print("=*"*40)

teste()
lista.append('cookie') # ADICIONAR NOVOS ELEMENTOS A LISTAS
teste()
lista.insert(0,'hotdog') #ADICIONAR NOVOS ELEMENTOS EM DETERMINADOS LOCAIS DAS LISTAS
teste()

# APAGAR ELEMENTOS
del lista[3] # OU lista.remove['pizza'] OU lanche.pop[3]
teste()
lista.pop() # REMOVE O ULTIMO ELEMENTO DA LISTA

#APAGAR SOMENTE SE O ELEMENTO ESTIVER NA LISTA
if 'hotdog' in lista:
    lista.remove('hotdog')
teste()

lista=[8,2,5,4,9,3,0]
print("ORDENAR LISTAS EM PYTHON")
lista.sort()
teste()

print("ORDENAR LISTAS EM ORDEM REVERSA")
lista.sort(reverse=True)
teste()

print("SOMAR ELEMENTOS LISTA")
teste()
print(len(lista))

print("PEGAR CHAVE E VALOR DA LISTA")
for c, v in enumerate(lista):
    print(f' chave:{c} e valor:{v}')
teste()

print("PEGAR VALORES PELO TECLADO")
lista = []
for cont in range(0,5):
    lista.append(int(input(f"informe o {cont} valor: ")))
teste()
