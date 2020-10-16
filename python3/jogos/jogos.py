import forca
import adivinhacao

def escolhe_jogo():
    print("*********************************")
    print("*******Escolha seu jogo!*********")
    print("*********************************")

    print("1 - forca;    2 - adivinhação")

    jogo = int(input("Qual jogo? "))

    if (jogo == 1):
        print("Jogo da forca")
        forca.jogar()
    else if(jogo == 2):
        print("Jogando adivinhação")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()
