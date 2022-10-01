import random

pl_num = 1
print("Enter total numbers of players")
total_pl = int(input())
score_list = [0]*total_pl

while True:
    # step 1: I randomly generate number and
    # add it to current score of current player
    print("Player-", pl_num, ", Press ENTER to roll the dice ")
    input()
    score = random.randint(1,6)
    print("You rolled :", score)
    score_list[pl_num-1] = score_list[pl_num-1] + score

    curr_pl_score = score_list[pl_num-1]

    # step 2: first of all, i Directly check for winning
    if curr_pl_score == 100:
        print("Player", pl_num,"Wins...!")
        break

    if curr_pl_score > 100:
        print("Opps.. No effect... ")
        curr_pl_score = curr_pl_score - score
        print("You need", (100-curr_pl_score), "to win...")

    # step 3: I check for all ladders
    if curr_pl_score == 4:
        print("Woooo... You got ladder at 4. Climb up at 56")
        curr_pl_score = 56
    elif curr_pl_score == 12:
        print("Woooo... You got ladder at 12. Climb up at 50")
        curr_pl_score = 50
    elif curr_pl_score == 14:
        print("Woooo... You got ladder at 14. Climb up at 55")
        curr_pl_score = 55
    elif curr_pl_score == 22:
        print("Woooo... You got ladder at 22. Climb up at 58")
        curr_pl_score = 58
    elif curr_pl_score == 41:
        print("Woooo... You got ladder at 41. Climb up at 79")
        curr_pl_score = 79
    elif curr_pl_score == 54:
        print("Woooo... You got ladder at 54. Climb up at 88")
        curr_pl_score = 88

    # step 4: lets for snakes
    if curr_pl_score == 28:
        print("Oppppssss... You ate by Snake at 28. Move down at 10")
        curr_pl_score = 10
    elif curr_pl_score == 37:
        print("Oppppssss... You ate by Snake at 37. Move down at 3")
        curr_pl_score = 3
    elif curr_pl_score == 47:
        print("Oppppssss... You ate by Snake at 47. Move down at 16")
        curr_pl_score = 16
    elif curr_pl_score == 75:
        print("Oppppssss... You ate by Snake at 75. Move down at 32")
        curr_pl_score = 32
    elif curr_pl_score == 94:
        print("Oppppssss... You ate by Snake at 94. Move down at 71")
        curr_pl_score = 71
    elif curr_pl_score == 96:
        print("Oppppssss... You ate by Snake at 96. Move down at 42")
        curr_pl_score = 42

    score_list[pl_num-1] = curr_pl_score

    if score==6:
        print("You rolled 6.. Repeat your turn..")
        continue

    if score!=6:
        pl_num = pl_num + 1
    if pl_num>total_pl:
        print("Round complete: ", score_list)
        pl_num = 1

