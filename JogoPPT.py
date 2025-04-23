import random
req = input("Deseja jogar? S/N: ")
# looping
while True:

    if req.upper() == "N":
        print("Obrigado por jogar! )")
        break
    elif req.upper() != "S":
        print("Opção inválida. Digite apenas S ou N.")
        req = input("Deseja jogar? S/N: ")
    # opcao de jogo
    print("Qual opcao deseja jogar?")
    print("Se deseja jogar Player x Player digite 1.")
    print("Se for Player x Bot digite 2.")
    print("Se for Bot x Bot digite 3.")
    opcao = int(input("DIGITE SUA OPÇÃO: "))
    
    # Player X Player
    if opcao == 1:
        print("Bem Vindo ao Jokempo digital!!")

        Player1 = input("Player 1, Escolha pedra, papel ou tesoura: ").lower()
        Player2 = input("Player 2, Escolha pedra, papel ou tesoura: ").lower()

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
        
    # Player X Bot
    elif opcao ==2:
        print("Bem Vindo ao Jokempo digital!!")
        
        playerVsB = input("Escolha entre: pedra, papel ou tesoura: ").lower() # Opção do player
        botVsP = random.randint(1,3) # Opção do Bot
        
        # Conversão de número para jogada do bot
        if botVsP == 1:
            botVsP = "pedra"
        elif botVsP == 2:
            botVsP = "papel"
        elif botVsP == 3:
            botVsP = "tesoura"

        print (f"O Bot escolheu {botVsP}")

        # Possíveis resultados
        if playerVsB == botVsP:
            print("Ocorreu um empate!")
        elif botVsP == "tesoura" and playerVsB == "pedra":
            print("O jogador venceu!")
        elif botVsP == "tesoura" and playerVsB == "papel":
            print("O Bot venceu! Mais sorte na próxima.")
        elif botVsP == "pedra" and playerVsB == "tesoura":
            print("O Bot venceu! Mais sorte na próxima.")
        elif botVsP == "pedra" and playerVsB == "papel":
            print("O jogador venceu!")
        elif botVsP == "papel" and playerVsB == "pedra":
            print("O Bot venceu! Mais sorte na próxima.")
        elif botVsP == "papel" and playerVsB == "tesoura":
            print("O Jogador venceu!")

    elif opcao == 3:
        print("Bem Vindo ao Jokempo digital!!")
    # parte do pedrinho 
    # BOT X BOT, nao posso usar lista lascou 
    # aleatorio
        bot1 = random.randint(0,2)

        # gambiarra do diabo
        if bot1 == 0:
            bot1Res = "pedra"
        elif bot1 == 1:
            bot1Res = "papel"
        elif bot1 == 2:
            bot1Res = "tesoura"
        print("o bot1 escolheu " + bot1Res)

        # copia e cola
        bot2 = random.randint(0,2)

        # gambiarra do diabo
        if bot2 == 0:
            bot2Res = "pedra"
        elif bot2 == 1:
            bot2Res = "papel"
        elif bot2 == 2:
            bot2Res = "tesoura"
        print("o bot2 escolheu " + bot2Res)

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

    req = input("deseja continuar jogando? ")