import random

def jogar_adivinhacao():
    print("------------------------------")
    print("Bem vindo o jogo de advinhação!")
    print("------------------------------")

    random.seed(100)
    numero_secreto = random.randrange(1,101)

    rodada = 1
    tentativas = 0
    pontos = 1000

    print("Qual o nivel de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Escolha o nível: "))

    if(nivel == 1):
        tentativas = 10
    elif(nivel == 2):
        tentativas = 5
    else:
        tentativas = 3

    for rodada in range(1,tentativas + 1):
        print("Tentativa {} de {}".format(rodada, tentativas))
        numer

        o = input("Digite um número de 0 a 100: ")

        chute = int(numero)

        if(chute < 1 or chute > 100):
            print("Por favor, digite um numero entre 1 e 100")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
             print("você acertou e fez {} pontos!".format(pontos))
             break
        else:
            if (maior):
                print("você errou, seu numero é maior que o numero secreto")
            elif (menor):
                print("Você errou, seu numero é menor que o numero secreto")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

    print("Fim do jogo!")

if(__name__=="__main__"):
    jogar_adivinhacao()