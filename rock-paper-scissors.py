import random

continue_game = True
first_step = True
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

while continue_game:
    
    #while first_step:

        #try:
    print(f"Enter a value between 1 and 3: 1 Rock, 2 Paper and 3 Scissors")
    players_choice = int(input(">"))

    if players_choice == 1:
        players_choice_value = "Rock"
        first_step = False

    elif players_choice == 2:
        players_choice_value = "Paper"
        first_step = False

    elif players_choice == 3:
        players_choice_value = "Scissors"
        first_step = False

    else:
        print(f"Please select a valid value")
                
        # except ValueError:
        #     print(f"Non numeric values are not allowed")
        #     continue
    
    print(
        f"The computer has chosen {program_choice_value} and you have chosen {players_choice_value}"
    )
    
    if program_choice == players_choice:
        print(f"That's a tie!")
        
    elif program_choice == 1 and players_choice == 2:
        print(f"You win!!")
        
    elif program_choice == 1 and players_choice == 3:
        print(f"You lose!")

    elif program_choice == 2 and players_choice == 1:
        print(f"You lose!")

    elif program_choice == 2 and players_choice == 3:
        print(f"You win!!")
        
    elif program_choice == 3 and players_choice == 1:
        print(f"You win!!")

    elif program_choice == 3 and players_choice == 2:
        print(f"You lose!!")
    

