import random

def play_game():
    options = ["rock", "paper", "scissors"]
    user_score = 0
    comp_score = 0

    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice not in options:
            print("Invalid choice. Please try again.")
            continue

        comp_choice = random.choice(options)
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {comp_choice}")

        if user_choice == comp_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and comp_choice == "scissors") or \
             (user_choice == "scissors" and comp_choice == "paper") or \
             (user_choice == "paper" and comp_choice == "rock"):
            print("You win!")
            user_score += 1
        else:
            print("You lose!")
            comp_score += 1

        print(f"Scores - You: {user_score}, Computer: {comp_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    play_game()
