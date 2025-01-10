#programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from  random import randint
from time import sleep

partida = []
contador = []
cont = 0

while True:
    contador.append('x')
    jogos = []
    empate = total_empates = quant = 0
    nomes_empat = []
    ganhador = []
    num_partida = {}
    ganhador_dados = {}
    temp = {}
    cont += 1

    for c in range(0, len(contador)):
        partida.append(f'{c}')

    print('---'*30)
    print(f'Quantidade de jogadores: 2 ou 4')
    quant = int(input('>>> '))

    if quant != 2:
        while True:
            if quant != 2:
                if quant == 4:
                    break
                if quant != 4:
                    quant = int(input(f'Opção inexistente! Tente novamente: '))
            if quant == 2:
                break

    if quant == 2:

        for c in range(0,2):
            temp['nome'] = str(input(f'Nome do jogador(a) {c+1}: '))
            temp['dado'] = randint(1,6)

            jogos.append(temp.copy())
            temp.clear()

        print('Bora para o Jogo!')
        print()

        for c in range(0,2):
            print(f'Jogando o dado do jogador {jogos[c]['nome']}...'), sleep(2)
            print(jogos[c]['dado'])

        for j in range(0,len(jogos)):

            if j == 0:

                maior = jogos[j]['dado']
                ganhador_dados['nome'] = jogos[j]['nome']
                ganhador_dados['dado'] = jogos[j]['dado']
                num_partida[f'{cont}'] = ganhador_dados.copy()

            elif jogos[j]['dado'] > maior:

                ganhador_dados['nome'] = jogos[j]['nome']
                ganhador_dados['dado'] = jogos[j]['dado']
                num_partida[f'{cont}'] = ganhador_dados.copy()

                nomes_empat.clear()
                maior = jogos[j]['dado']

            elif jogos[j]['dado'] == maior:

                empate = 1
                nomes_empat.append(jogos[j]['nome'])
                ganhador_dados['nome'] = nomes_empat.copy()

        print()
        print(f'A maior número foi: {maior}!')

        if empate == 1:
            print(f'O jogo empatou e os dois jogadores venceram!')

        elif empate == 0:
            print(f'O ganhador foi o jogador(a) {ganhador_dados['nome']}')

        print('---'*30)
        resp = str(input('Deseja jogar novamente? [S/N] ')).upper().split()[0]

        if resp == 'N':
            break


    elif quant == 4:

        for c in range(0, 4):
            temp['nome'] = str(input(f'Nome do jogador(a) {c + 1}: '))
            temp['dado'] = randint(1, 6)

            jogos.append(temp.copy())
            temp.clear()

        print('Bora para o Jogo!')
        print()

        for c in range(0, 4):
            print(f'Jogando o dado do jogador {jogos[c]['nome']}...'), sleep(2)
            print(jogos[c]['dado'])

        for j in range(0, len(jogos)):

            if j == 0:

                maior = jogos[j]['dado']
                ganhador_dados['nome'] = jogos[j]['nome']

            elif jogos[j]['dado'] > maior:

                nomes_empat.clear()
                maior = jogos[j]['dado']
                ganhador_dados['nome'] = jogos[j]['nome']
                ganhador_dados['dado'] = jogos[j]['nome']

            elif jogos[j]['dado'] == maior:

                if empate == 0:
                    empate += 1
                    total_empates += 1
                    nomes_empat.append(jogos[j]['nome'])

                elif empate >= 1:
                    if jogos[j]['dado'] == maior:
                        nomes_empat.append(jogos[j]['nome'])
                        ganhador_dados['nome'] = nomes_empat.copy()
                        empate += 1
                        total_empates += 1

        num_partida[f'partida{cont}'] = ganhador_dados.copy()

        print('---'*30)
        print(f'A maior número foi {maior}!')

        if total_empates >= 1:
            print(f'Tivemos um total de {total_empates} empates')

        elif empate >= 1:
            for c in range(1, len(partida)):
                if ganhador == maior:
                    print(f'Os vencedores são {ganhador_dados['nome']}!')

        elif empate == 0:
            print(f'O vencedor é {ganhador_dados['nome']}!')

        print('---'*30)
        resp = str(input('Deseja jogar novamente? [S/N] ')).upper().split()[0]

        if resp == 'N':
            break

print(ganhador)
print(f'Jogo finalizado com sucesso! Você jogou um total de {cont} partidas')
print('Os ganhadores foram:')
print('---'*20)
print(f'{'Partida':^4} | {'Ganhadores':^20}')

for c in range(1,len(partida)):
    print(f'{c:^4} {num_partida[f'partida{c}']['nome']}')