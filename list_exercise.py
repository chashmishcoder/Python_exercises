
""""
# exercise 1
alist = [100,200,300,400,500]
alist.reverse()
print("Updated list is : ",alist)

"""

"""
# exercise 2
list1 = [5,10,15,20,25,50,20]
a = list1.index(20)
if 20 in list1:
    list1[a]= 200
    print("Updated list : ",list1)
else:
    print("20 is not present")

"""

"""
#exercise 3

list1=["M","na","i","Ke"]
list2 = ["y","me","s","lly"]
list3 = []
a =list1.index("M")
b = list2.index("y")
c = list1.index("na")
d = list2.index("me")
e =list1.index("i")
f = list2.index("s")
g =list1.index("Ke")
h = list2.index("lly")
list3.append(str(list1[a])+str(list2[b]))
list3.append(str(list1[c])+str(list2[d]))
list3.append(str(list1[e])+str(list2[f]))
list3.append(str(list1[g])+str(list2[h]))

print(list3)

"""

"""
# exercise 4

alist = [1,2,3,4,5,6,7]
i = 1
while i<=7:
    a = alist.index(i)
    sq = alist[a]*alist[a]
    alist[a]=sq
    i=i+1
alist.sort()
print(alist)

"""
"""
# exercise 5
list1 = ["Hello","take"]
list2 = ["Dear","Sir"]
list3 = []

a = list1.index("Hello")
b = list1.index("take")
c = list2.index("Dear")
d = list2.index("Sir")

list3.append(str(list1[a])+" "+str(list2[c]))
list3.append(str(list1[a])+" "+str(list2[d]))
list3.append(str(list1[b])+" "+str(list2[c]))
list3.append(str(list1[b])+" "+str(list2[d]))
print(list3)
"""

"""
# exercise 6
list1 = [10,20,30,40]
list2=[100,200,300,400]

list2.reverse()
i=0
while i<len(list1):
    print(str(list1[i]) + " " + str(list2[i]))
    i = i+1

"""
"""
# exercise 7

list1 = ["Mike","","Emma","Kelly","","Brad"]
list1.remove("")
list1.remove("")
print(list1)

"""

"""
# exercise 8
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].insert(2,7000)
print(list1)
"""

"""
#exercise 9

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
list2 = ["h", "i", "j"]
i = 0
while i<3:
    list1[2][1][2].insert(3,list2[i])
    list1[2][1][2].sort()
    i = i+1
print(list1)
"""

"""
# exercise 10

list1 = [5, 20, 15, 20, 25, 50, 20]
list1.remove(20)
list1.remove(20)
list1.remove(20)
print(list1)

"""

"""
# exercise 11

list1 = ['abc', 'xyz', 'aba', '1221' , 'xyyxz' , 'AA']
i = 0
count = 0
while i<len(list1):
    a = len(list1[i])
    if a>=3:
        if list1[i][0] == list1[i][-1]:
            count=count + 1
    i = i+1
print(count)

"""
