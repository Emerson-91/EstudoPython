"""dados = {'nome':'Pedro', 'idade': 25}
print(dados['nome'])
print()
dados['sexo']='masculino'
print(dados)
del dados['idade']
print(dados)
print()
filme = {'titulo':'Star wars', 'ano': 1977, 'diretor': 'George lucas'}
print(filme.values())
print(filme.keys())
print(filme.items())
print()
for k, v in filme.items():
    print( 'O {} é {}'.format(k,v))

locadora = {}
locadora.get(filme)

print(locadora)"""

pessoas = {'nome':'Emerson', 'sexo': 'M', 'idade':'28'}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print()

for k, v in pessoas.items():
    print(f'{k} = {v}')

print()
print()

estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('unidade federativa: '))
    estado['Sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())
print()
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()












