""" Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatorios.
Guarde esses resultados em um dicionario. N o final, coloque esse dicionario em ordem
 sabendo que o vencedor tirou o maior numero dado """
from random import randint
from  time import sleep
from operator import itemgetter

jogo = {'jogador1':randint(1, 6),'jogador2':randint(1, 6),'jogador3':randint(1,6),'jogador4':randint(1,6)}
ranking = list()
print('Valore Sorteados: ')
for k, v in jogo.items():
    print(f'O {k} tirou {v}')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('Ranking dos Sorteados')

for i, v in enumerate(ranking):
    print(f'O {i+1}  Lugar: {v[0]} com {v[1]}')
    sleep(1)




