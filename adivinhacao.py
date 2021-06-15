import random


# Jogo da Adivinhação
def adivinhacao_f():

    pontos = 1000
    abertura()

    x = random.randrange(1, 101, 1)  # Número Secreto

    qtd = dificuldade_jogo()
    sistema_jogo(qtd, x, pontos)

    dados_form(x)
    jogar_novamente()


def abertura():
    # Boas-vindas!
    print('-=' * 12)
    print('* Jogo da Adivinhação! *')
    print('-=' * 12)


def dificuldade_jogo():
    qtd = 0
    while True:
        print('Qual a dificuldade?')
        nivel = int(input('(1) Fácil / (2) Médio / (3) Difícil\n'))

        if nivel == 1:
            qtd = 10
            break
        elif nivel == 2:
            qtd = 7
            break
        elif nivel == 3:
            qtd = 5
            break
        else:
            print('Digite um valor válido!')
            print('-=' * 12)
            continue
    return qtd


def sistema_jogo(qtd, x, pontos):
    for i in range(1, qtd + 1, 1):
        try:
            print(f'Tentativa {i} de {qtd}')
            number = int(input('Digite um número entre 1 e 100: '))
            if number < 1 or number > 100:
                continue

            if number == x:
                print(f'Você acertou e fez {pontos} pontos!!')
                break
            else:
                if number > x:
                    print(f'Seu chute foi maior que o valor escolhido!')
                    print('-=' * 21)
                else:
                    print(f'Seu chute foi menor que o valor escolhido!')
                    print('-=' * 21)
                pontos -= abs(x - number)

        except ValueError:
            print('Valor Inválido! Digite um número!')


def dados_form(x):
    print(f'O número era {x}')
    print('Fim de jogo!')
    print('-=' * 15)


def jogar_novamente():
    # Jogar novamente
    novamente = str(input('Deseja jogar novamente? (S/N)\n').upper().strip())
    if novamente == 'S':
        adivinhacao_f()


# Rodar o jogo independente
if __name__ == '__main__':
    adivinhacao_f()