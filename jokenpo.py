import random

print('Vamos jogar jokenpo!' + '\n')

placar_vc = 0
placar_maquina = 0
tentativa = 0

while True:
    jogadas = ['pedra', 'papel', 'tesoura']


    usuário = str(input('Escolha entre pedra papel ou tesoura: ')).lower()
    maquina = random.choice(jogadas)

    while usuário not in jogadas:
        usuário = str(input('Escolha entre pedra, papel ou tesoura: ')).lower()

    jogada_maquina = print('A máquina jogou: '.format(maquina))
    print(maquina)


    if usuário == maquina:
        print('Empate!')
        placar_vc = placar_vc + 0
        placar_maquina = placar_maquina + 0
        tentativa += 1

    if usuário == 'pedra' and maquina == 'papel':
        print('A Máquina ganhou!')
        placar_vc = placar_vc + 0
        placar_maquina = placar_maquina + 1
        tentativa += 1

    if usuário == 'pedra' and maquina == 'tesoura':
        print('Você ganhou!')
        placar_vc = placar_vc + 1
        placar_maquina = placar_maquina + 0
        tentativa += 1

    if usuário == 'tesoura' and maquina == 'papel':
        print('Você ganhou!')
        placar_vc = placar_vc + 1
        placar_maquina = placar_maquina + 0
        tentativa += 1

    if usuário == 'tesoura' and maquina == 'pedra':
        print('A Máquina ganhou!')
        placar_vc = placar_vc + 0
        placar_maquina = placar_maquina + 1
        tentativa += 1

    if usuário == 'papel' and maquina == 'pedra':
        print('Você ganhou!')
        placar_vc = placar_vc + 1
        placar_maquina = placar_maquina + 0
        tentativa += 1

    if usuário == 'papel' and maquina == 'tesoura':
        print('A Máquina ganhou!')
        placar_vc = placar_vc + 0
        placar_maquina = placar_maquina + 1
        tentativa += 1

    if tentativa % 5 ==0:
        continuar = str(input('Você quer continuar jogando? S/N ')).upper()
        opcoes_continuar = ['S','N']
        while continuar not in opcoes_continuar:
            continuar = str(input('Você quer continuar jogando? S/N ')).upper()

        if continuar == 'N':
            break

print('O placar final é: Você fez {0} pontos e a Máquina fez {1} pontos.'.format(placar_vc,placar_maquina))
if placar_vc > placar_maquina:
    print('Você ganhou!')
    quit()
if placar_maquina > placar_vc:
    print('A Máquina ganhou!')
    quit()
if placar_maquina == placar_vc:
    print('O jogo terminou em empate!')
    quit()



