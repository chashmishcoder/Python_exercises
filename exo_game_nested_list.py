def show_mat():
    i=1
    while i<=9:
        print(ls[i-1], end="  ")
        if i%3==0:
            print()
        i = i + 1

def check_winner():
    if ls[0] == ls[3] and ls[3] == ls[6]:
        return True
    elif ls[1] == ls[4] and ls[4] == ls[7]:
        return True
    elif ls[2] == ls[5] and ls[5] == ls[8]:
        return True
    elif ls[0] == ls[1] and ls[1] == ls[2]:
        return True
    elif ls[3] == ls[4] and ls[4] == ls[5]:
        return True
    elif ls[6] == ls[7] and ls[7] == ls[8]:
        return True
    elif ls[0] == ls[4] and ls[4] == ls[8]:
        return True
    elif ls[2] == ls[4] and ls[4] == ls[6]:
        return True
    else:
        return False


ls = [[1,2,3],[4,5,6],[7,8,9]]
pl = 1
sym = "X"
count=0

show_mat()

while True:
    print("Player",pl,"- Enter box number")
    box_num = int(input())
    if ls[box_num-1]!= 'X' and ls[box_num-1]!='O':
        ls[box_num-1] = sym
    else:
        print("Invalid Box Selected")
        print("Please Repeat your turn")
        show_mat()
        continue
    show_mat()
    winner_found = check_winner()

    if winner_found == True:
        print("Player", pl, "Wins...!" )
        break
    elif winner_found == False:
        count = count + 1
        if count==9:
            print("Match Draw..!")
            break
        if pl==1:
            pl=2
            sym = 'O'
        elif pl==2:
            pl=1
            sym = 'X'

