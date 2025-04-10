import random

req = input("deseja Jogar? S/N ")
#looping
while True:
    if req != "S":
        break
    #opcao de jogo
    opcao = int(input("qual opcao deseja jogar?, se for player x player digite 1, se for player x bot digite 2, se for bot x bot digite 3, DIGITE SUA OPCAO"))
 

    if opcao == 1:
        print("Bem Vindo ao Jokempo digital!!")

        Player1 = input("Player 1, Escolha pedra, papel ou tesoura:")
        Player2 = input("Player 2, Escolha pedra, papel ou tesoura:")

        if Player1 == Player2:
            print("Vocês empataram")

        elif Player1 == "pedra" and Player2 == "tesoura":
            print("Player 1 Ganhou!")
        elif Player1 == "pedra" and Player2 == "papel":
            print("Player 2 Ganhou!")
        elif Player1 == "papel" and Player2 == "pedra":
            print("Player 1 Ganhou!!")
        elif Player1 == "papel" and Player2 == "tesoura":
            print("Player 2 Ganhou!!")
        elif Player1 == "tesoura" and Player2 == "papel":
            print("Player 1 Ganhou!")
        elif Player1 == "tesoura" and Player2 == "pedra":
            print("Player 2 Ganhou!!")
        
    elif opcao ==2:
        print("nao tem ainda")
    elif opcao == 3:
    #parte do pedrinho 
    # BOT X BOT, nao posso usar lista lascou 
    #aleatorio
        bot1 = random.randint(0,2)

        # gambiarra do diabo
        if bot1 == 0:
            bot1Res = "pedra"
        elif bot1 == 1:
            bot1Res = "papel"
        elif bot1 == 2:
            bot1Res = "tesoura"
        print("o bot1 escolheu " + bot1Res)

        #copia e cola
        bot2 = random.randint(0,2)

        # gambiarra do diabo
        if bot2 == 0:
            bot2Res = "pedra"
        elif bot2 == 1:
            bot2Res = "papel"
        elif bot2 == 2:
            bot2Res = "tesoura"
        print("o bot2 escolheu " + bot1Res)

        if bot1 == bot2:
            print("Eles empataram!")
        elif bot1 != bot2:
            if bot1 == 0 and bot2 == 1:
                print("bot2 venceu")
            elif bot1 == 0 and bot2 == 2:
                print("bot1 venceu")
            #acaba pelo amor de deus, q coisa feia
            elif bot1 == 1 and bot2 == 0:
                print("bot1 venceu")
            elif bot1 == 1 and bot2 == 2:
                print("o bot2 venceu")
            elif bot1 == 2 and bot2 == 1:
                print("o bot1 venceu")
            elif bot1 == 2 and bot2 == 0:
                print("o bot2 venceu")


    req = input("deseja continuar jogando?")
