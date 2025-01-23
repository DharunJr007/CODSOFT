import random

def play_game():
    ch = ["rock", "paper", "scissors"]
    u_s = 0
    c_s = 0

    while True:
        u_c = input("Choose rock, paper, or scissors: ").lower()
        if u_c not in ch:
            print("Invalid choice. Please try again.")
            continue

        c_c = random.choice(ch)
        print(f"You chose: {u_c}")
        print(f"Computer chose: {c_c}")

        if u_c == c_c:
            print("It's a tie!")
        elif (u_c == "rock" and c_c == "scissors") or \
             (u_c == "scissors" and c_c == "paper") or \
             (u_c == "paper" and c_c == "rock"):
            print("You win!")
            u_s += 1
        else:
            print("You lose!")
            c_s += 1

        print(f"Scores - You: {u_s}, Computer: {c_s}")

        p_a = input("Do you want to play again? (yes/no): ").lower()
        if p_a != "yes":
            break

if __name__ == "__main__":
    play_game()
