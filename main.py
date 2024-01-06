import random as rd
import numpy as np
import os


start = False
class First_Player:
    def __init__(self, name = None):
        self.name = name
        self.mark = "X"
        self.first = False
        self.second = False
        self.guess = False
class Second_Player:
    def __init__(self, name = None):
        self.name = name
        self.mark = "O"
        self.first = False
        self.second = False
        self.guess = False

class Board:
    board = np.array([[" ", " ", " "],
                     [" ", " ", " "],
                     [" ", " ", " "]])
    
    def move_x(self, row, column):
        row -= 1
        column -= 1
        self.board[row, column] = "X"
        return print(self.board)
    
    def move_o(self, row, column):
        row -= 1
        column -= 1
        self.board[row, column] = "O"
        return print(self.board)
    
    def cancel_move(self, row, column):
        row -= 1
        column -= 1
        self.board[row, column] = " "
        return print(self.board)
    
game_board = Board()

first_name = input("What is first player name?\n: ")
second_name = input("What is second player name?\n: ")
P1 = First_Player(first_name)
P2 = Second_Player(second_name)

def check_win(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i, j] == player.mark for j in range(3)) or all(board[j, i] == player.mark for j in range(3)):
            return True
    if all(board[i, i] == player.mark for i in range(3)) or all(board[i, 2 - i] == player.mark for i in range(3)):
        return True
    return False

re = 0
while re < 1:
    re += 1
    answer = input("Do you want to flip a coin or choose randomly to determine who will start first? (Flip Coin/Random)\n: ")
    if answer.lower() == "flip coin" or answer.lower() == "flip a coin":
        coin_side = rd.randint(0,1)
        if coin_side == 0:
            result = "head"
        else:
            result = "tail"
        player_guess = rd.randint(0,1)
        if player_guess == 0:
            P1.guess = True
        else:
            P2.guess = True
        print("\nThe result of the random outcome will determine whether Player One or Player Two gets to pick the coin side.")
        if P1.guess == True:
            who_guess = P1
            not_guess = P2
        else:
            not_guess = P1
            who_guess = P2
        print(f"\n{who_guess.name} has to pick the coin side!")
        re_ask = 0
        while re_ask < 1:
            re_ask += 1
            Player_Guess = input(f"{who_guess.name} guess ( Head or Tail ) ?\n\n: ")
            if Player_Guess.lower() == result:
                print("Luckly the coin is in the head side!")
                print(f"{who_guess} goes first!")
                first = who_guess
                second = not_guess
                start = True
            elif Player_Guess.lower() != "head" and (Player_Guess.lower() != "tail" or Player_Guess.lower() == "tails"):
                print("wrong spelling!")
                re_ask -= 1
            elif Player_Guess.lower() == "quit":
                break
            else:
                first = not_guess
                second = who_guess
                print(f"{not_guess.name} goes first!")
                start = True
        
    elif answer.lower() == "random":
        random = rd.randint(0,1)
        if random == 1:
            first = P1
            second = P2
            print(f"{P1.name} goes first!")
            start = True
        else:
            first = P2
            second = P1
            print(f"{P2.name} goes first!")
            start = True
    elif answer.lower() == "quit":
        break
    else:
        print("\nPlease type filp coin or random!!\n")
        re -= 1

gb = game_board
win1 = gb.board[0,0],gb.board[0,1],gb.board[0,2]
win2 = gb.board[1,0],gb.board[1,1],gb.board[1,2]
win3 = gb.board[2,0],gb.board[2,1],gb.board[2,2]
win4 = gb.board[0,0],gb.board[1,0],gb.board[2,0]
win5 = gb.board[0,1],gb.board[1,1],gb.board[2,1]
win6 = gb.board[0,2],gb.board[1,2],gb.board[2,2]
win7 = gb.board[0,0],gb.board[1,1],gb.board[2,2]
win8 = gb.board[0,2],gb.board[1,1],gb.board[2,0]
possible_win = [win1, win2, win3, win4, win5, win6, win7, win8]
valid_move = [1,2,3]
if start == True:
    check = False
    count = 0
    while count != 10:
        if count == 0:
            for i in range(3):
                if all(gb.board[i,j] for j in range(3)) != " " == False:
                    print("It's a tie!!")
                    count = 10
                    start = False
                    break
            print(f"\n\n{first.name} turn!\n")
            print(gb.board)
            try :
                row = int(input(f"Please select row (1 - 3)\n {first.name}: "))
            except ValueError:
                print("\nPlease type number!!")
                row = None
                break
            try :
                column = int(input(f"Please select column (1 - 3)\n {first.name}: "))
            except ValueError:
                print("\nPlease type number!!")
                column = None
                break
            if row not in valid_move or column not in valid_move:
                print("Out of range!")
                break
            elif gb.board[row-1, column-1] == "O" or gb.board[row-1, column-1] == "X":
                print("It already has mark in position!")
                break
            else:
                gb.move_x(row, column)
                count = 1
                answer_2 = input("Do you want to confirm move? (Y/N)\n: ")
                if answer_2.lower() == "n" or answer_2.lower() == "no":
                    gb.cancel_move(row,column)
                    count = 0
                else:
                    if check_win(gb.board, first) == True:
                        print(f"\n\n{first.name} win!!")
                        count = 10
                        start = False
                        break
                    else:
                        pass
            
        elif count == 1:
            for i in range(3):
                if all(gb.board[i,j] for j in range(3)) != " " == False:
                    print("It's a tie!!")
                    count = 10
                    start = False
                    break
            print(f"\n\n {second.name} turn!\n")
            print(gb.board)
            try :
                row = int(input(f"Please select row (1 - 3)\n {second.name}: "))
            except ValueError:
                print("\nPlease type number!!")
                row = None
            try :
                column = int(input(f"Please select column (1 - 3)\n {second.name}: "))
            except ValueError:
                print("\nPlease type number!!")
                column = None
            if row not in valid_move or column not in valid_move:
                print("Out of range!")
            elif gb.board[row-1, column-1] == "O" or gb.board[row-1, column-1] == "X":
                print("\n It already has a mark in this position!")
            else:
                gb.move_o(row, column)
                count = 0
                answer_2 = input("Do you want to confirm move? (Y/N)\n: ")
                if answer_2.lower() == "n" or answer_2.lower() == "no":
                    gb.cancel_move(row,column)
                    count = 1
                else:
                    if check_win(gb.board, second) == True:
                        print(f"\n\n{second.name} win!!")
                        count = 10
                        start = False
                        break
                    else:
                        pass
                    