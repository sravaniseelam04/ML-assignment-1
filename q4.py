it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# length of the it_companies
length_it = len(it_companies)
print("the length og the set it_companies  is;", length_it)

# adding twitter to the set it_companies
it_companies.add("twitter")
print(it_companies)
# adding multiple it companies to the set.
multi_ITcompanies= ["Tesla","Samsung", "Deloitte"]
it_companies.update(multi_ITcompanies)
print(it_companies)
# removing google from the set
it_companies.remove("Google")
print(it_companies)

# what is the difference between remove and discard.

# discard : in discard method, if the element  is not present in the set , it dosent throw any exception.

# remove: in remove method, if the element is not present , it throws  an exception.

# join A and B

C = A.union(B)
print(C)

#Find A intersection B
i = A.intersection(B)
print(i)

#Is A subset of B
s = A.issubset(B)
print(s)

#Are A and B disjoint sets
d = A.isdisjoint(B)
print(d)

#Join A with B and B with A
D = B.union(A)
print(C)
print(D)

#What is the symmetric difference between A and B
sd = A.symmetric_difference(B)
print(sd)

#Delete the sets completely
 
del A,B

#Convert the ages to a set and compare the length of the list and the set.

AGE = set(age)
print(len(age)==len(AGE))
