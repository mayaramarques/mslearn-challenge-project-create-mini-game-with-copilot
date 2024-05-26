import random

def game():
    player_score = 0
    computer_score = 0
    while True:
        player = input("Rock, Paper or Scissors? ").lower()
        computer = random.choice(["rock", "paper", "scissors"])
        print(f"Player: {player}")
        print(f"Computer: {computer}")

        if player == computer:
            print("It's a tie!")
        elif player == "rock":
            if computer == "scissors":
                print("You win!")
                player_score += 1
            else:
                print("You lose!")
                computer_score += 1
        elif player == "paper":
            if computer == "rock":
                print("You win!")
                player_score += 1
            else:
                print("You lose!")
                computer_score += 1
        elif player == "scissors":
            if computer == "paper":
                print("You win!")
                player_score += 1
            else:
                print("You lose!")
                computer_score += 1
        elif player == "rock":
            if computer == "scissors":
                print("You win!")
                player_score += 1
        else:
            print("Invalid input!")

        print(f"Player score: {player_score}")
        print(f"Computer score: {computer_score}")

        while True:
            play_again = input("Do you want to play again? (yes/no) ").lower()
            if play_again == "yes":
                break
            elif play_again == "no":
                print("Thanks for playing!")
                return
            else:
                print("Invalid input! Please enter 'yes' or 'no'.")
                continue

game()

