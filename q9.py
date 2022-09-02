import math
number = int(input("number of students:"))
A = [] # for weight in lbs from user
B = [] # list kg weights
for i in range(number):
    A.append(int(input()))
for b in A:
    a = (math.floor((b/2.2046)*100))/100# formulae for converting from lbs to kgs.
    B.append(a)
print(B)