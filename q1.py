ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24,21]

#Sort the list and find the min and max age
ages.sort
print("the ages list after sorting",ages)
print("mininum of the ages in the list is:", min(ages))
print("maximun of the ages in the list is:", max(ages))

#Add the min age and the max age again to the list
ages.append(19)
ages.append(26)
print("the list after adding the min and max ages again:", ages)

#Find the median age (one middle item or two middle items divided by two)
length = len(ages)
if length%2 == 0:
    median=(ages[length//2] + ages[(length//2)-1])/2
    print('the median of the ages is :', median)

else:
    median = (ages[length//2])
    print(median)
total = 0
for i in range(0, length):
    total = total + ages[i]

#Find the average age (sum of all items divided by their number)
print("the average of the ages in the list:", total//length)

#Find the range of the ages (max minus min)
range = max(ages) - min(ages)
print("the range of the list is ", range)
