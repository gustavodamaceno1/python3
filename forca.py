def jogar_forca():
    print("--------------------------------")
    print("---Bem vindo ao jogo da Forca---")
    print("--------------------------------")

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    print(palavras)

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Qual a letra? ")
        chute = chute.strip().upper()

        index = 0
        if(chute in palavra_secreta):
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print("Ops, voce errou! Faltam {} tentativas".format(6-erros))

        if(erros == 6):
            break
        if("_" not in letras_acertadas):
            break
        print(letras_acertadas)

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas

    if("_" not in letras_acertadas):
        print(palavra_secreta)
        print("Você Ganhou!")
    else:
        print(palavra_secreta)
        print("Você perdeu!!")

    print("Fim do jogo!")

if(__name__=="__main__"):
    jogar_forca()