
def jogar():

    print("*********************************")
    print("*********Jogo da forca!**********")
    print("*********************************")

    palavra_secreta = "python"
    letras_acertadas = ['_', '_', '_', '_', '_', '_']

    enforcou = False
    acertou = False

    print(letras_acertadas)

    while(not enforcou and not acertou): #palavras chaves sempre em minúsculo

        chute = input("Qual letra?")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
                #print("Encontrei a letra {} na posição {}".format(letra,index))
            index++

        print(letras_acertadas)


    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
