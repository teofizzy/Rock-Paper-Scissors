import random
import os

CHOICES = ["R", "P", "S"]


def user_input(action: str = None):
    if action == "play":
        prompt = "Would you like to play? [Y = Yes, N = No]: "

        choices = ["Y", "N"]

        choice = validate_input(prompt, choices)

        if choice == "Y":
            choice = True
        else:
            choice = False

    else:
        prompt = (
            "Enter your choice from the following [R = Rock, P = Paper, S = Scissors]: "
        )

        choice = validate_input(prompt, CHOICES)

    # Return the valid choice
    return choice


def validate_input(prompt, CHOICES):
    while True:
        # Prompt uer to input their choice
        choice = input(prompt).upper()

        # Validate the user input
        if choice in CHOICES:
            break
        else:
            print("Invalid Guess. Try Again!\n")

    return choice


def evaluate_choices(user_choice, computer_choice):
    print(f"\nPlayer Choice: {user_choice} | Computer Choice: {computer_choice}\n")

    # Check for a draw
    if user_choice == computer_choice:
        return print("\nIt's a draw!")

    # Check if User won
    elif (
        (user_choice == "R" and computer_choice == "S")
        or (user_choice == "P" and computer_choice == "R")
        or (user_choice == "S" and computer_choice == "P")
    ):
        return print(f"\nPlayer Wins. Congratulations!")

    # Otherwise, the Computer wins
    else:
        return print(f"\nComputer Wins. Better luck next time :(")


def main():
    print("Welcome to the Rock Paper Scissors game!\n")

    while user_input(action="play"):
        os.system("clear")

        print("You are now playing the Rock Paper Scissors game!\n")

        # 1. Get the user input
        user_choice = user_input()

        # 2. Get the computer choice
        computer_choice = random.choice(CHOICES)

        # 3. Evaluate the choices and return winner and loser
        evaluate_choices(user_choice, computer_choice)

    print("\nThank you! See you next time :)")


if __name__ == "__main__":
    main()
