# Declaring an empty list
ls = []

# nested list logic
i=1
while i<=3:
    ls.append([])
    i = i+1

# inserting elements in list
i=1
while i<=9:
    if i<=3:
        ls[0].append(i)
    elif i<=6:
        ls[1].append(i)
    else:
        ls[2].append(i)
    i = i+1

# printing the list
print(ls)
