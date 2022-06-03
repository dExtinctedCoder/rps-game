import random

print('''******************+++++++ WELCOME TO THE GAME +++++++******************\n''')
  

rules = input("Do you wish to read the game rules?    Y for (yes)  N for (no)\n")
rules = rules.upper()

if rules == "Y":
    print('''\nWhat are the rules of RPS?
The rules to play it are pretty simple.
The game is played against the CPU where you use the pre-built functions to make a move that will represent the elements of the game; rock, paper and scissors. The outcome of the game is determined by 3 simple rules:

Rock wins against scissors.
Scissors win against paper.
Paper wins against rock.\n''')

elif rules == "N":
    pass

else:
    print("Invalid input")
    exit()
    
print('''_________Instructions__________
 Enter: 
    (R) for Rock
    (P) for Paper
    (S) for Scissors
  \n''')


def input_validation():
    try:
        int(init)

    except ValueError:
        print("Player character can only be a number")


def play():
    start_game = False
    move = ["R", "P", "S"]

    while not start_game:

        player_move = input("Enter your move: ")
        player_move = player_move.upper()

        if player_move:
            if player_move != 'R' and player_move != 'S' and player_move != 'P':
                print("Invalid input. Please choose from the options provided\n")
                play()
        else:
            print("Input cannot be empty\n")
            play()

        cpu = random.choice(move)
        move_index = move.index(cpu)
        cpu_move = move[move_index]
        print("Cpu move: " + cpu_move + '\n')
        print("`Player (%s) : Cpu (%s)`\n" % (player_move, cpu_move))

        if player_move == cpu_move:
            print("Game is a tie\n")

        elif (cpu_move == "P" and player_move == "R") or (cpu_move == "R" and player_move == "S") or (
                cpu_move == "S" and player_move == "P"):
            print("Cpu wins\nTry harder next time")
            exit()

        elif (player_move == "P" and cpu_move == "R") or (player_move == "R" and cpu_move == "S") or (
                player_move == "S" and cpu_move == "P"):
            print("Player%d wins\nCongratulations" % character)
            exit()


is_input_valid = False
while not is_input_valid:

    init = input("\nEnter player character you wish to play as: \n(1) Player 1 \n(2) Player 2 \n(3) Player 3 \n")
    input_validation()

    if init:
        if init == "1":
            character = 1
            print("\nLogged in as Player %d\nStart game\n" % character)
            is_input_valid = True
            play()
        elif init == "2":
            character = 2
            print("\nLogged in as Player %d\nStart game\n" % character)
            is_input_valid = True
            play()
        elif init == "3":
            character = 3
            print("\nLogged in as Player %d\nStart game\n" % character)
            is_input_valid = True
            play()
        else:
            print("Character unavailable. Please choose from the available characters\n")
    else:
        print('Player character cannot be empty\n')
        is_input_valid = False
