#tic tac toe!
[spot11,spot12,spot13]=[" "," "," "]
[spot21,spot22,spot23]=[" "," "," "]
[spot31,spot32,spot33]=[" "," "," "]
X="X"
O="O"

import random

def update_board(): #updating the board
    print(spot11," | ",spot12," | ",spot13)
    print("———+—————+———")
    print(spot21," | ",spot22," | ",spot23)
    print("———+—————+———")
    print(spot31," | ",spot32," | ",spot33)
    
def show_positions():
    print(1," | ",2," | ",3)
    print("———+—————+———")
    print(4," | ",5," | ",6)
    print("———+—————+———")
    print(7," | ",8," | ",9)
    
def ask_for(letter):
    print("If you would like to see the positions, type 'positions'")
    position=input("Where will you put your "+str(letter)+"? ")
    while position=="positions" or int(position) not in range(1,10):
        if position=="positions":
            show_positions()
            position=input("Where will you put your "+str(letter)+"? ")
        else:
            print("Invalid position. Try again. If you would like to see the positions, type 'positions'")
            position=input("Where will you put your "+str(letter)+"? ")
    return [int(position),letter]

def correlate_position(letter):
    [position,letter]=ask_for(letter)
    if position==1:
        modified=spot11
    if position==2:
        modified=spot12
    if position==3:
        modified=spot13
    if position==4:
        modified=spot21
    if position==5:
        modified=spot22
    if position==6:
        modified=spot23
    if position==7:
        modified=spot31
    if position==8:
        modified=spot32
    if position==9:
        modified=spot33
    return [position,modified]

def get_valid_spot(letter):
    if letter==X:
        team=team_x
    elif letter==O:
        team=team_o
    print("It is now",team+"'s turn.")
    [position,spot]=correlate_position(letter)
    while spot=="X" or spot=="O":
        print("This spot is already taken! Try again.")
        [position,spot]=correlate_position(letter)
    return int(position)

def starting_team():
    x=random.random()
    o=random.random()
    if x>o:
        return team_x
    return team_o

def check_for_winner():
    row1=[spot11,spot12,spot13]
    row2=[spot21,spot22,spot23]
    row3=[spot31,spot32,spot33]
    col1=[spot11,spot21,spot31]
    col2=[spot12,spot22,spot32]
    col3=[spot13,spot23,spot33]
    diag1=[spot11,spot22,spot33]
    diag2=[spot13,spot22,spot31]
    
    if row1==[X,X,X] or row2==[X,X,X] or row3==[X,X,X]\
       or col1==[X,X,X] or col2==[X,X,X] or col3==[X,X,X]\
       or diag1==[X,X,X] or diag2==[X,X,X]:
        return team_x
    if row1==[O,O,O] or row2==[O,O,O] or row3==[O,O,O]\
       or col1==[O,O,O] or col2==[O,O,O] or col3==[O,O,O]\
       or diag1==[O,O,O] or diag2==[O,O,O]:
        return team_o
    if " " not in row1 and " " not in row2 and " " not in row3:
        return "filled"
    return None

def switch_turn():
    if turn==team_x:
        return team_o
    return team_x

#The actual game:
print("Welcome to Tic Tac Toe!")
team_x=input("Team X, name your team: ")
team_o=input("Team O, name your team: ")
starting_team=starting_team()

print("Based on a random coin toss, the starting team will be",starting_team+"!")
print("The board has these positions. You can currently choose to put your letter in any position")
show_positions()
print()

turn=starting_team
x_spot=0
o_spot=0

while check_for_winner()!=team_x and check_for_winner()!=team_o:
    if check_for_winner()=="filled":
        break
    
    print("The current board looks like this:")
    update_board()
    print()
    
    if turn==team_x:
        x_spot=get_valid_spot("X")
    else:
        o_spot=get_valid_spot("O")

    #changing X's spot
    if x_spot==1:
        spot11="X"
    if x_spot==2:
        spot12="X"
    if x_spot==3:
        spot13="X"
    if x_spot==4:
        spot21="X"
    if x_spot==5:
        spot22="X"
    if x_spot==6:
        spot23="X"
    if x_spot==7:
        spot31="X"
    if x_spot==8:
        spot32="X"
    if x_spot==9:
        spot33="X"
        
    #changing O's spot
    if o_spot==1:
        spot11="O"
    if o_spot==2:
        spot12="O"
    if o_spot==3:
        spot13="O"
    if o_spot==4:
        spot21="O"
    if o_spot==5:
        spot22="O"
    if o_spot==6:
        spot23="O"
    if o_spot==7:
        spot31="O"
    if o_spot==8:
        spot32="O"
    if o_spot==9:
        spot33="O"
        
    turn=switch_turn()
    print()

print()
update_board()
print() 

if check_for_winner()==team_x:
    print("The winner is",team_x+"! Congratulations :)")
elif check_for_winner()==team_o:
    print("The winner is",team_o+"! Congratulations :)")
else:
    print("Both teams have tied! Better luck next time.")
