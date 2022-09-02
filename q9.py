import math
number = int(input("number of students:"))
A = []
B = []
for i in range(number):
    A.append(int(input()))
for b in A:
    a = (math.floor((b/2.2046)*100))/100;