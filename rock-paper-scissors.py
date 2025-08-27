import random
import sys

program_score = 0
player_score = 0
ties = 0

while True:

    # Computer choice
    program_choice = random.randint(1, 3)

    if program_choice == 1:
        program_choice_value = "Rock"

    elif program_choice == 2:
        program_choice_value = "Paper"

    else:
        program_choice_value = "Scissors"

    # Player input with validation
    try:
        print(f"Enter a value between 1 and 4: 1 Rock, 2 Paper, 3 Scissors and 4 Quit")
        players_choice = int(input(">"))

        if players_choice == 1:
            players_choice_value = "Rock"

        elif players_choice == 2:
            players_choice_value = "Paper"

        elif players_choice == 3:
            players_choice_value = "Scissors"

        elif players_choice == 4:
            sys.exit()

        else:
            print(f"\nPlease select a valid value\n")

    except ValueError:
        print(f"\nNon numeric values are not allowed\n")
        continue

    # Show choices
    print(
        f"The program has chosen {program_choice_value} and you have chosen {players_choice_value}\n"
    )

    # Determine winner
    if players_choice == program_choice:
        print("It's a tie!")
        ties += 1
    elif (
        (players_choice == 1 and program_choice == 3)
        or (players_choice == 2 and program_choice == 1)
        or (players_choice == 3 and program_choice == 2)
    ):
        print("You win!")
        player_score += 1
    else:
        print("You lose!")
        program_score += 1

    print(f"\nPlayer {player_score} --- Program {program_score} --- Ties {ties}\n")
