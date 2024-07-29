# File : CS112_A1_T2_2_20231052
"""
Purpose: In Number Scrabble, players select numbers from a list ranging from 1 to 9 in turns. Once chosen, a number cannot be selected again.
The game concludes in three scenarios: a player wins by selecting three numbers that sum up to 15, all numbers are picked without any player achieving a sum of 15, resulting in a draw, or a player picks three numbers that sum up to 15 before all numbers are chosen, leading to a win.
"""
# Author: Dareen Elsayed Ragab
# ID: 20231052


# Welcome message and display instructions
def welcome_instructions():
    print("*** welcome to number scrabble game ***")
    print("")
    print("""
The game's instructions
1- Number scrabble is played with the list of numbers between 1 and 9.
2- Each player takes turns picking a number from the list.
3- Once a number has been picked, it cannot be picked again.
4- If a player has picked three numbers that add up to 15, that player wins the game.
5- If all the numbers are used and no player gets exactly 15, the game is a draw.""")
    print("")
    # starting the game
    input("Press enter to start the game....")
    print("")



# verify number range of player1,2
def check_valid_input(player_total,n):
    while True:
        try:
            player = int(input(f"player{n}: enter a number between 1 and 9: "))
            if player in list_of_game:
                player_total.append(player)
                list_of_game.remove(player)
                break
            else:
                print("Error: this number is not in range of the list! ")
        except ValueError:
            print("INVALID: You need to enter an integer number only! ")

# to check which player won
def check_win(player_total):
    player_total.sort()  # Sort the list(ascending order of the list)
    n = len(player_total)
    for i in range(n - 2): # example [1,2,4,5,6]
        left = i + 1
        right = n - 1
        while left < right:
            current_sum = player_total[i] + player_total[left] + player_total[right]
            if current_sum == target:
                All_lists_of_players()
                return True
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    return False
# to print all lists of players
def All_lists_of_players():
    print("")
    print(f"All numbers of player1: {player1_total}")
    print(f"All numbers of player2: {player2_total}")
    print("-" * 40)

# main program
player1_total = []
player2_total = []
target = 15
welcome_instructions()

# list to pick a number
list_of_game = [1, 2, 3, 4, 5, 6, 7, 8, 9]
while True:
    print("")
    print(f"Available numbers: {list_of_game}")
    player_1 = check_valid_input(player1_total,1) # player1 input and verify valid input
    if check_win(player1_total):
        print("Player1 wins!")
        exit()
    elif len(list_of_game) == 0:
        break


    print("")
    print(f"Available numbers: {list_of_game}")
    player_2 = check_valid_input(player2_total,2) # player 2 input and verify valid input
    if check_win(player2_total):
        print("Player2 wins!")
        exit()

All_lists_of_players()
print("The game is a draw!")
exit()












