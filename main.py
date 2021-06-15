import adivinhacao
import forca

while True:
    try:
        print('-=' * 10)
        print(f'* Escolha o Jogo! *')
        print('-=' * 10)

        jogo = int(input('(1) Advinhação / (2) Forca / (3) Sair\n'))

        if jogo == 1:
            adivinhacao.adivinhacao_f()
        elif jogo == 2:
            forca.forca_f()
        elif jogo == 3:
            break
        else:
            raise ValueError
    except ValueError:
        print('Valor inválido!! Digite Novamente!')

print('Você foi embora! :( ')
