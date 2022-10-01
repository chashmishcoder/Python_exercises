import random
global out
global ls
def ladders():
    global lad

    print(lad)
def player():
    global ls
    i = 1
    player = 1
    score = 0
    while i <= no_of_players:
        print(player, "Play your turn")
        input("Press enter to roll dice")
        out = random.randint(1, 6)
        score = score + out
        ls.append(score)
        if len(ls)>no_of_players:
            ls.append(out)

        score = 0
        print("You got", out)
        player = player + 1
        i = i + 1
        print(ls)


ls = []
print("Enter numbers of players playing the game")
no_of_players = int(input())
lad = list(range(1,101))
while True:
    player()


