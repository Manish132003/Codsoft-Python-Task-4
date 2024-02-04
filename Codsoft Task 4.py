import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def rock_paper_scissors_game():
    user_score = 0
    computer_score = 0

    while True:
        print("\nRock, Paper, Scissors Game")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Quit")

        user_choice = input("Enter your choice (1/2/3/4): ").lower()

        if user_choice == '4':
            print("Thanks for playing. Final Scores:")
            print(f"You: {user_score} | Computer: {computer_score}")
            break

        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)

        if user_choice in ['1', '2', '3']:
            user_choice = choices[int(user_choice) - 1]
            result = determine_winner(user_choice, computer_choice)
            print(f"\nYou chose {user_choice}. Computer chose {computer_choice}.")
            print(result)

            if result == "You win!":
                user_score += 1
            elif result == "Computer wins!":
                computer_score += 1
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    rock_paper_scissors_game()
