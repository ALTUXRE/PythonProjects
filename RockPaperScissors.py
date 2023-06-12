Choices = ("rock", "paper", "scissors")
running = True

while running:

    player1=input("player1 (rock, paper, scissors): ")
    while player1 not in Choices:
        player1 = input("player1 (rock, paper, scissors): ")
    player2=input("player2 (rock, paper, scissors): ")
    while player2 not in Choices:
        player2 = input("player2 (rock, paper, scissors): ")

    if player1 == player2:
        print("It's a tie!")
    elif player1 == "rock" and player2 == "scissors":
        print("player1 wins!")
    elif player1 == "paper" and player2 == "rock":
        print("player1 wins!")
    elif player1 == "scissor" and player2 == "paper":
        print("player1 wins!")
    else:
        print("player2 wins!")

    if not input("Play again? (y/n): ").lower() == "y":
        running = False

print("Thanks for playing!")
