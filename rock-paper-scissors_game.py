# ROCK-PAPER-SCISSORS GAME
import random
import time

option = ['rock', 'paper', 'scissors']
rock = option[0]
paper = option[1]
scissors = option[2]

print('Welcome to rock-paper-scissors game, Press "q" to end the game')

while True:
    choice = input('select rock or paper or scissors: ')
    pc_choice = random.choice(option)
    if choice == rock:
        if pc_choice == rock:
            print('pc choice: rock \n result: DRAW')
        elif pc_choice == scissors:
            print('pc choice: scissors \n result: WON')
        else:
            print('pc choice: paper \n result: LOST')
    if choice == paper:
        if pc_choice == paper:
            print('pc choice: paper \n result: DRAW')
        elif pc_choice == rock:
            print('pc choice: rock \n result: WON')
        else:
            print('pc choice: scissors \n result: LOST')
    if choice == scissors:
        if pc_choice == scissors:
            print('pc choice: scissors \n result: DRAW')
        elif pc_choice == rock:
            print('pc choice: rock \n result: LOST')
        else:
            print('pc choice: paper \n result: WON')
            
    if choice == 'q':
            print('exiting...')
            time.sleep(1)
            break
            
     
