import time
import random

nums = ['1','2','3','4','5','6','7','8','9']
opr = ["+", "-", "*"]

print("Enter Total numbers of players")
total_players = int(input())
time_list = []

round = 1
while round<=total_players:
    print("Player", round, ", Ready...?")
    print("Press ENTER to start your turn")
    input()
    st_time = time.perf_counter()
    # questions starts from here
    question=1
    while question<=3:
        a = random.choice(nums)
        b = random.choice(nums)
        op = random.choice(opr)
        while True:
            q = a + op + b
            oans = eval(q)
            print("Question No.",question)
            print(q)
            uans = int(input())
            if uans == oans:
                question = question + 1
                print("Correct Answer...!")
                break
            else:
                print("Wrong Answer, Try Again..!")
                continue
    else:
        end_time = time.perf_counter()
        total_time = end_time - st_time
        time_list.append(total_time)
        round = round + 1
        print("Total Time taken :", total_time)

min_time = min(time_list)
winner_ind = time_list.index(min_time)
print("Player-", (winner_ind+1), "wins...!")


