global a
global i
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Logic of matrix
def matrix():
    i = 0
    while i < 9:
        if i < 3:
            print(a[i], end="  ")
        elif i >= 3 and i < 6:
            if i == 3:
                print(sep="")
            if i >= 3 and i < 6:
                print(a[i], end="  ")
        else:
            if i == 6:
                print(sep="")
            print(a[i], end="  ")
        i = i + 1

def player_1():
    print("\nPlayer 1, Enter your Number :", end="")
    choice = int(input())
    if choice == 1 and 1 in a:
        a[0] = "X"
        print()
        matrix()

    elif choice == 2 and 2 in a:
        a[1] = "X"
        print()
        matrix()

    elif choice == 3 and 3 in a:
        a[2] = "X"
        print()
        matrix()

    elif choice == 4 and 4 in a:
        a[3] = "X"
        print()
        matrix()

    elif choice == 5 and 5 in a:
        a[4] = "X"
        print()
        matrix()

    elif choice == 6 and 6 in a:
        a[5] = "X"
        print()
        matrix()

    elif choice == 7 and 7 in a:
        a[6] = "X"
        print()
        matrix()

    elif choice == 8 and 8 in a:
        a[7] = "X"
        print()
        matrix()

    elif choice == 9 and 9 in a:
        a[8] = "X"
        print()
        matrix()

    else:
        print("Invalid Move, Please enter a valid number")
        matrix()
        player_1()

def player_2():
    print("\nPlayer 2, Enter your Number :", end="")
    choice_2 = int(input())
    if choice_2 == 1 and 1 in a:
        a[0] = "O"
        print()

    elif choice_2 == 2 and 2 in a:
        a[1] = "O"
        print()

    elif choice_2 == 3 and 3 in a:
        a[2] = "O"
        print()

    elif choice_2 == 4 and 4 in a:
        a[3] = "O"
        print()

    elif choice_2 == 5 and 5 in a:
        a[4] = "O"
        print()

    elif choice_2 == 6 and 6 in a:
        a[5] = "O"
        print()

    elif choice_2 == 7 and 7 in a:
        a[6] = "O"
        print()

    elif choice_2 == 8 and 8 in a:
        a[7] = "O"
        print()

    elif choice_2 == 9 and 9 in a:
        a[8] = "O"
        print()

    else:
        print("Invalid Move, Please enter a valid number")
        matrix()
        player_2()



print("Welcome to EXO Game","\U0001F92B")
print("Rules")
print("1- Player 1 will select a number from matrix and will be replaced by letter X")
print("2- Player 2 will select a number from matrix and will be replaced by letter O")
print("3- The first one to get three consecutive letters in one line will win the game.")
print("****************************")
print("Game starts: ")
while True:
    matrix()
    player_1()
    if a[0] is a[1] is a[2]:
        print("\nCongratulations, Player 1 wins the game")
        break
    elif a[3] is a[4] is a[5]:
        print("\nCongratulations, Player 1 wins the game")
        break
    elif a[6] is a[7] is a[8]:
        print("\nCongratulations, Player 1 wins the game")
        break
    elif a[0] is a[3] is a[6]:
        print("\nCongratulations, Player 1 wins the game")
        break
    elif a[1] is a[4] is a[7]:
        print("\nCongratulations, Player 1 wins the game")
        break
    elif a[2] is a[5] is a[8]:
        print("\nCongratulations, Player 1 wins the game")
        break
    elif a[0] is a[4] is a[8]:
        print("\nCongratulations, Player 1 wins the game")
        break
    elif a[2] is a[4] is a[6]:
        print("\nCongratulations, Player 1 wins the game")
        break
    elif str(1) not in str(a[0]) and str(2) not in str(a[1]) and str(3) not in str(a[2]) and str(4) not in str(a[3]) and str(5) not in str(a[4]) and str(6) not in str(a[5]) and str(7) not in str(a[6]) and str(8) not in str(a[7]) and str(9) not in str(a[8]):
        print()
        print("\nOH! NO..... Tie game :(")
        break



    player_2()
    if a[0] is a[1] is a[2]:
        print("\nCongratulations, Player 2 wins the game")
        break
    elif a[3] is a[4] is a[5]:
        print("\nCongratulations, Player 2 wins the game")
        break
    elif a[6] is a[7] is a[8]:
        print("\nCongratulations, Player 2 wins the game")
        break
    elif a[0] is a[3] is a[6]:
        print("\nCongratulations, Player 2 wins the game")
        break
    elif a[1] is a[4] is a[7]:
        print("\nCongratulations, Player 2 wins the game")
        break
    elif a[2] is a[5] is a[8]:
        print("\nCongratulations, Player 2 wins the game")
        break
    elif a[0] is a[4] is a[8]:
        print("\nCongratulations, Player 2 wins the game")
        break
    elif a[2] is a[4] is a[6]:
        print("\nCongratulations, Player 2 wins the game")
        break