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
            elif Player_Guess.lower() != "head" and Player_Guess.lower() != "tail":
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
        


if start == True:
    count = 0
    print(f"{first.name} turn!\n")
    print(game_board.board)
    while count != 10:
        if count == 0:
            count += 1
            row = int(input(f"Please select row (1 - 3)\n {first.name}: "))
            column = int(input(f"Please select column (1 - 3)\n {first.name}: "))
            game_board.move_x(row, column)
            answer_2 = input("Do you want to confirm move? (Y/N)\n: ")
            if answer_2.lower() == "n" or answer_2.lower() == "no":
                count = 0
                game_board.cancel_move(row,column)

