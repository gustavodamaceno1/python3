import random

def jogar_forca():

    abertura_jogo()
    palavra_secreta = carregar_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        chute = pede_chute()

        if(chute in palavra_secreta):
            marcar_chute(chute,letras_acertadas,palavra_secreta)
        else:
            erros += 1
            forca_erros(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        mensagem_vencendor()
    else:
        mensagem_perdeu()

    print("Fim do jogo!")

def abertura_jogo():
    print("--------------------------------")
    print("---Bem vindo ao jogo da Forca---")
    print("--------------------------------")
    
    
def carregar_palavra_secreta():
    palavras = []
    with open("palavras.txt") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def pede_chute():
    chute = input("Qual a letra? ")
    chute = chute.strip().upper()
    return chute

def marcar_chute(chute,letras_acertadas,palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def mensagem_vencendor():
    print("Parabéns, você Ganhou!")

def mensagem_perdeu(palavra_secreta):
    print("Você perdeu, foi enforcado!!")
    print("A palavra secreta era {}".format(palavra_secreta))

def forca_erros(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()
if(__name__=="__main__"):
    jogar_forca()
