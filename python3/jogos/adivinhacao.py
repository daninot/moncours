import random

def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    #numero_secreto = round(random.random() * 100)
    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("1 - fácil;  2 - médio;  3 - difícil")
    nivel = int(input(" "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas+1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute = input("Digite um número entre 1 e 100: ") # só que o input vai ler uma string
        print("You typed ", chute_str)
        #agora preciso converter a string em int, porque não posso comparar duas coisas diferentes
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100.")
            continue


        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):     # a partir desse : tudo o que vem depois ta dentro do if
            print("You won! e fez {} pontos!".format(pontos))           # mas é necessário deixar identado (com tab)
            break
        else:
            if(maior):
                print("You lose! Seu chute foi maior que o número secreto.")
            elif(menor):
                print("You lose! Seu chute foi menor que o número secreto.")

            pontos_perdidos = abs(numero_secreto - chute)   #pra não ter número negativo
            pontos = pontos - pontos_perdidos


    print("Game over")          #tudo o que estiver identado depois do else vai estar dentro dele, pra "sair" é só sair da identação

if(__name__ == "__main__"):     #essa linha é pro arquivo executar separado no terminal, sem ter que executar o jogos.py pra jogar
    jogar()
