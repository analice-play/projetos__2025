#programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogadores = []

while True:
    jogador = {}
    gols = []
    gols_partida = {}
    cont = 0

    jogador['nome'] = str(input('Nome do jogador: '))
    jogador['num_jogador'] = int(input(f'Nº da camiseta do jogador {jogador['nome']}: '))
    jogador['quant_partidas'] = int(input('Quantidade de partidas: '))

    for c in range(0, 21):

        if c == jogador['quant_partidas']:
            gols_total = 0

            for i in range(1, (c+1)):
                cont += 1

                gols1 = int(input(f'Quantidade de gols na partida {i}: '))
                gols.append(gols1)

                gols_total += gols1
                gols_partida[f'partida{cont}'] = gols.copy()
                jogador['gols_partida'] = gols_partida.copy()

                gols.clear()

    aproveitamento = (jogador['quant_partidas'] / gols_total) * 100

    jogador['gols_total'] = gols_total
    jogadores.append(jogador.copy())

    resp = str(input('Deseja adicionar mais algum jogador? [S/N] ')).upper().split()[0]

    if resp == 'N':
        break
print(jogadores)
print()
print('---'*30)
print(f"{'NÚMERO':^8} | {'NOME':^20} | {'PARTIDAS':^10} | {'GOLS':^8} | {'APROVEITAMENTO':^15}")
print(f"{jogador['num_jogador']:^8} | {jogador['nome']:<20} | {jogador['quant_partidas']:^10} | {jogador['gols_total']:^8} |    {aproveitamento}%")

print('\nDeseja ver os dados de forma mais ampla? [S/N] ')
resp = str(input('>>> ')).upper().split()[0]

cont = 1

if resp == 'S':
    opção = int(input('Número do jogador: '))

    for c in range(0, (len(jogadores) + 1)):

        if jogadores[c]['num_jogador'] == opção:
            print(f"{f'Dados do jogador {jogadores[c]['nome']}':^30}")

            cont1 = c

            while True:
                while jogadores[c]['quant_partidas'] > cont:

                    print(f"O jogador teve {jogadores[cont1]['gols_partida'][f'partida{cont}']} gols na Partida {cont}")

                    cont += 1
                if cont == jogadores[cont1]['quant_partidas']:
                    break

        elif c == ( len(jogadores) + 1 ):

            print('\033[31mOpção não existente! Tente novamente?')
            opção = int(input('Número do jogador: '))


print('\nPrograma finalizado com sucesso!')