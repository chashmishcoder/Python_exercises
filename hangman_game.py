import random
#empty list
ls = []
#answers list
ls_2= ["india","europe","america","korea","brazil","rome","paris","london","england","ireland"]
a = random.randint(0,9)
word=ls_2[a]
i=1
while i<=len(word):
    ls.append("_")
    i=i+1
print("Welcome To Hangman Game","\U0001F92B")
print("Rules:")
print("1 - Player has only 6 chances to guess the letters")
print("2- If player guesess all the letters before chances get out, player wins")
print("3- If not then computer wins")
print("***************************************************************************")
print("Game Starts Here")
print()
print(ls)
chances = len(word)
j=len(word)
while j<=chances:

    print("Guess the letter or word :- ",end="")
    guess = input()
    if guess=="":
        print("**NOTE :- Enter valid letter")

    elif guess in word:
        s =0
        while s<len(word)-1:
            v = word.find(guess,s)
            ls[v]=ls_2[a][v]
            s=s+1
            if ls == ls_2[a]:
                print("you Win..")
                break
        print(ls)

    else:
        chances = chances - 1
        print(guess,"is not correct letter. You have ",chances,"chances left.")
        print("**************************************************")
        if chances==0:
            print("You have exceeded your attempts, You lost the game...")
            print("The word was "+ word)
            print("Computer won the game, Better luck next time...")
            break
        print(ls)

    j=j-1
