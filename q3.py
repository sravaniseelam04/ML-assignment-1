#Create a tuple containing names of your sisters and your brothers
sisters = ("shivani","radha","ramya","lekha")
brothers = ("ram","laxman","rahul","ravi")

#Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers
print(siblings)

#number of siblings
number_of_siblings = len(siblings)
print("total number of siblings :", number_of_siblings)

#Modify the siblings tuple and add the name of your father and mother and assign it to family_members
mother = " tirupathamma"
father = " seeta rami reddy"

family_members = list(siblings)

family_members.append(mother)
family_members.append(father)

print("all family numbers: ", family_members)


