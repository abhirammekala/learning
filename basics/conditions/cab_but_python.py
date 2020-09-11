from random import randint
from time import sleep

def be_different():
    global num1, num2, num3
    if num1 == num2 or num1 == num3 or num2 == num3:
        num1 = (randint(1, 9))
        num2 = (randint(1, 9))
        num3 = (randint(1, 9))
        be_different()

num1 = randint(1, 9)
num2 = randint(1, 9)
num3 = randint(1, 9)
be_different()
eheheh = True
while eheheh == True:
    numone = input("what is number 1? \n")
    numtwo = input("what is number 2? \n")
    numthree = input("what is number 3? \n")
    print('please wait XD')
    sleep(randint(1,3))
    