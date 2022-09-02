ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24,21]
ages.sort
print("the ages list after sorting",ages)
print("mininum of the ages in the list is:",min(ages))
print("maximun of the ages in the list is:",max(ages))
ages.append(19)
ages.append(26)
print("the list after adding the min and max ages again:",ages)
length = len(ages)
if length%2 == 0:
    median=(ages[length//2] + ages[(length//2)-1])/2
    print('the median of the ages is :',median)

else:
    median=(ages[length//2])
    print(median)
total = 0
for i in range(0,length):
    total = total + ages[i]
print("the average of the ages in the list:",total//length)
range = max(ages) - min(ages)
print("the range of the list is ",range)
