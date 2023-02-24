"""
Um jogo de adivinhação é um jogo onde o objetivo é adivinhar algum tipo de informação, 
como uma palavra, uma frase, um título ou a localização de um objeto, neste caso números.
"""


import random

def jogar():
    print ("****************************************")
    print ("****Bem Vindo ao Jogo da Adivinhação****")
    print ("****************************************", end ='\n\n')


    print ("Descubra o numero secreto ")
    print ("Você deve digitar um número entre 1 e 100\n\n")
    print ("Escolha o nivel de dificuldade: ")
    print ("(1) Facil, (2) Médio, (3) Dificl", end='\n\n')

    nivel= int(input("Defina o nivel: "))

    # numero = round(random.random()*100) essa função gera um numero aleatoreio entre 0 e 100#
    numero = round(random.randrange(1,101)) #random.randrange() gera um numero aleatorio entre 1 e 100#
    tentativa = 0
    pontos=100

    if(nivel==1):
        print("Nivel (1) Facil, Você tem 20 tentativas !! ")
        tentativa= 20
    elif(nivel==2):
        print("Nivel (2) Medio, Você tem 10 tentativas !!")
        tentativa=10
    else:
        print("Nivel (3) Dificil, Você tem 5 tentativas !! {}")
        tentativa=5


    for rodada in range(1,tentativa+1):
        print ("\nRODADA - {} de {}".format(rodada,tentativa))
        chute=int(input("Digite um numero: "))
        if(chute==numero):
            print("Você acertou!!")
            break
        else:
            if(chute <1 or chute >100):
                print("Valor Invalido")
                print ("Tente novamente com valores entre 1 e 100", end='\n')
                continue

            elif(chute<numero):
                print("Seu numero e menor que o numero secreto")

            elif(chute>numero):
                print("Seu numero e maior que o numero secreto")
        n_pontos= abs(numero - chute)  #função abs() calcula e retorna sempre numeros positivo
        pontos = pontos - n_pontos
        print("Tente Novamente.")

    print("Fim de Jogo!!")
    print("O numero secreto era = {}".format(numero))
    print("Você fez {} pontos".format(pontos))

if(__name__=="__main__"):
    jogar()
