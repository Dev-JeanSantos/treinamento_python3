from sys import _clear_type_cache


def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana".upper()
    palavras_acertadas = ["_","_","_","_","_","_"]
    enforcou = False
    acertou = False
    erro = 0
    print()
    print(palavras_acertadas)
    print()

    while(not enforcou and not acertou):

        chute = input("Qual é a letra? ")
        chute = chute.strip().upper()
        
        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    palavras_acertadas[index] = letra
                index += 1
        else:
            erro += 1
        enforcou = erro == 6
        acertou = "_" not in palavras_acertadas  
        print(palavras_acertadas)

    if(acertou):
        print("Parabéns voce ganhou o jogo!")
    else:
        print("Infelizmente voce perdeu o jogo!")
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
