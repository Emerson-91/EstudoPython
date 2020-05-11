""" Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
guardado em um dicionario, incluindo o total de gols feitos durante o campeonato"""

jogador = dict()
gol = list()
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for c in range(0,tot):
    gol.append(int(input(f'Quantos gols na partida {c+1}? ')))
jogador['gols'] = gol[:]
jogador['total'] = sum(gol)

for k, v in jogador.items():
    print(f' O campo {k} tem valor {v}')
print('-='*30)
print(f'o Jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')

for i, v in enumerate(jogador['gols']):
    print(f'   => na partida {i+1} fez {v} gols')
print(f'Foi um total de {jogador["total"]} gols.')
print(jogador)