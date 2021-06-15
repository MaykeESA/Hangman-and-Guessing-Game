import random


# Jogo da Forca
def forca_f():

    abertura()

    palavra_secreta = sistema_palavra_secreta()
    listaps = ['_' for letra in palavra_secreta]

    vida = dificuldade_jogo(palavra_secreta)
    dicas_form(palavra_secreta, listaps)
    sistema_jogo(palavra_secreta, listaps, vida)

    jogar_novamente()


def abertura():
    print('-=' * 9)
    print('* Jogo da Forca! *')
    print('-=' * 9)


def sistema_palavra_secreta():
    # Sistema de palvra secreta
    lista_palavras = ['Melancia', 'Turbo', 'Carro', 'Macaco', 'Batata', 'Pistão', 'Bruxo']
    x = random.randrange(0, len(lista_palavras), 1)
    palavra_secreta = lista_palavras[x].upper()
    return palavra_secreta


def dificuldade_jogo(palavra_secreta):
    while True:
        try:
            # Sistema de dificuldade
            print('Qual a dificuldade?')
            nivel = int(input('(1) Fácil / (2) Médio / (3) Difícil\n').strip())
            if nivel == 1:
                vida = len(palavra_secreta) + 3
                break
            elif nivel == 2:
                vida = len(palavra_secreta) + 2
                break
            elif nivel == 3:
                vida = len(palavra_secreta) + 1
                break
            else:
                raise ValueError

        except ValueError:
            print('Digite um número válido!!')
            print('-=' * 13)
    return vida


def dicas_form(palavra_secreta, listaps):
    print(f'A palavra possúi {len(palavra_secreta)} letras!')
    print(' '.join(listaps))
    print('-=' * 12)


def sistema_jogo(palavra_secreta, listaps, vida):
    while True:
        print(f'Você possúi {vida} vida(s)!!')
        tntletra = str(input(f'Digite uma letra: ').upper().strip())
        index = 0

        if tntletra in palavra_secreta:
            for letra in palavra_secreta:
                if tntletra == letra:
                    listaps[index] = letra
                index += 1
        else:
            vida -= 1

        print(' '.join(listaps))
        print('-=' * 12)

        if listaps.count('_') == 0:
            print(f'Você GANHOU!!')
            break

        elif vida == 0:
            print('Você PERDEU!!')
            print(f'A palavra era: {palavra_secreta}')
            break


def jogar_novamente():
    # Jogar novamente
    novamente = str(input('Deseja jogar novamente? (S/N)\n').upper().strip())
    if novamente == 'S':
        forca_f()


# Rodar o jogo independente
if __name__ == '__main__':
    forca_f()
