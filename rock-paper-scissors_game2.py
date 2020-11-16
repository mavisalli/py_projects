import random
import time

option = ['rock', 'paper', 'scissors']
rock = option[0]
paper = option[1]
scissors = option[2]

lost_right = 3
req_to_win = 0

print('Welcome to rock-paper-scissors game \n Whoever gets 3 time wins will win \n Press "q" to end the game')

while True:
    choice = input('select rock or paper or scissors: ')
    pc_choice = random.choice(option)
    if choice == rock:
        if pc_choice == rock:
            print('pc choice: rock \n result: DRAW')
        elif pc_choice == scissors:
            print('pc choice: scissors \n result: WON')
            req_to_win +=1
        else:
            print('pc choice: paper \n result: LOST')
            lost_right -=1
    if choice == paper:
        if pc_choice == paper:
            print('pc choice: paper \n result: DRAW')
        elif pc_choice == rock:
            print('pc choice: rock \n result: WON')
            req_to_win +=1
        else:
            print('pc choice: scissors \n result: LOST')
            lost_right -=1
    if choice == scissors:
        if pc_choice == scissors:
            print('pc choice: scissors \n result: DRAW')
        elif pc_choice == rock:
            print('pc choice: rock \n result: LOST')
            lost_right -=1
        else:
            print('pc choice: paper \n result: WON')
            req_to_win +=1
    if lost_right == 0:
        print(' GAME OVER!')
        time.sleep(5)
        break            
    elif req_to_win == 3:
        print('CONGRATULATİONS, YOU WİN')
        time.sleep(5)
        break
            
    if choice == 'q':
            print('exiting...')
            time.sleep(1)
            break
            