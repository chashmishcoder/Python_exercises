import random
import time
def expression():
    global exp
    nums = [1,2,3,4,5,6,7,8,9]
    opr = ["+","-","*","/","**"]
    a = random.choice(nums)
    b = random.choice(nums)
    op= random.choice(opr)
    print(a,op,b,end=" = ")
    exp = eval("a"+op+"b")





print("*Welcome to Quiz Game*")
print("Game Rules: ")
print("1 - Each player will get 5 questions to solve")
print("2 - If the answer is wrong, Re-Enter answer till it gets correct")
print("3 - The player which will solve the quiz in less time will win the game")
print("----------------------------------------------------------------------------------------------------\n")
print("Player 1 Turn")
expression()
i=1
while i<6:

    pl_1 = input()
    if str(pl_1)== str(exp):
        if i==5:
            break
        else:
            expression()
    else:
        while True:
            if str(pl_1) != str(exp):
                print("Incorrect answer, Please enter correct answer")

                continue
            else:
                break




    i=i+1


