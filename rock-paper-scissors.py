import random

continue_game = True
program_choice = random.randint(1, 3)

if program_choice == 1:
    program_choice_value = "Rock"

elif program_choice == 2:
    program_choice_value = "Paper"

else:
    program_choice_value = "Scissors"

print(
    f"(Debug): program_choice is {program_choice} and its value is {program_choice_value}"
)
print(f"Enter a value between 1 and 3: 1 Rock, 2 Paper and 3 Scissors")

try:
    players_choice = int(input(">"))
except ValueError:
    print(f"Non numeric values are not allowed")

while continue_game:

    try:
        print(f"Enter a value between 1 and 3: 1 Rock, 2 Paper and 3 Scissors")
        players_choice = int(input(">"))

        if players_choice == 1:
            players_choice_value = "Rock"

        elif players_choice == 2:
            players_choice_value = "Paper"

        elif players_choice == 3:
            players_choice_value = "Scissors"

        else:
            print(f"Please select a valid value")
            continue

    except ValueError:
        print(f"Non numeric values are not allowed")
        continue

print(
    f"(Debug): players_choice is {players_choice} and its value is {players_choice_value}"
)
