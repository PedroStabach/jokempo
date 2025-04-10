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
    