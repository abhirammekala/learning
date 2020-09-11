#Rock Paper Scissors Game
from random import randint
from time import sleep

ply_score = 0
cpu_score = 0
Wink = True
cpu_choiceAR = ["rock", "paper", "scissors"]
cpu_choice = 0
player_choice =0
while Wink == True:
    player_choice = input("rock paper or scissors?\n")
    cpu_choice = cpu_choiceAR[randint(0, 2)]
    print("please wait while computer makes choice eheheheh...")
    sleep(randint(1,3))
    print("The cpu chose : ", cpu_choice)
    sleep(.4003)
    if cpu_choice == "scissors" and (player_choice == "rock" or player_choice == "Rock"):
        print("hey! you won(your score increased by one)")
        ply_score += 1
        print("your score is ", ply_score, " the computers score is ", cpu_score)
    elif cpu_choice == 'rock' and (player_choice == "scissors" or player_choice == 'Scissors'):
        print("oof. the computer won :(the computer's score increased by one")
        cpu_score += 1
        print("your score is ", ply_score, " the computers score is ", cpu_score)
    if cpu_choice == "paper" and (player_choice == "rock" or player_choice == "Rock"):
        print("oof. the computer won :(the computer's score increased by one")
        cpu_score += 1
        print("your score is ", ply_score, " the computers score is ", cpu_score)
    elif cpu_choice == "rock" and (player_choice == 'paper' or player_choice == "paper"):
        print("hey! you won(your score increased by one)")
        ply_score += 1
        print("your score is ", ply_score, " the computers score is ", cpu_score)
    if cpu_choice == 'scissors' and (player_choice == "paper" or player_choice == "Paper"):
        print("oof. the computer won :(the computer's score increased by one")
        cpu_score += 1
        print("your score is ", ply_score, " the computers score is ", cpu_score)
    elif cpu_choice == "paper" and (player_choice == "scissors" or player_choice == "Scissors"):
        print("hey! you won(your score increased by one)")
        ply_score += 1
        print("your score is ", ply_score, " the computers score is ", cpu_score)
    if cpu_choice == "rock" and (player_choice == "rock" or player_choice == "Rock"):
        print("eheheheh...  the computer chose the same thing as you...(nobody's score increased)")
        print("your score is ", ply_score, " the computers score is ", cpu_score)
    if cpu_choice == "scissors" and (player_choice == "scissors" or player_choice == "Scissors"):
        print("eheheheh...  the computer chose the same thing as you...(nobody's score increased)")
        print("your score is ", ply_score, " the computers score is ", cpu_score)
    if cpu_choice == "paper" and (player_choice == "paper" or player_choice == "Paper"):
        print("eheheheh...  the computer chose the same thing as you...(nobody's score increased)")
        print("your score is ", ply_score, " the computers score is ", cpu_score)


