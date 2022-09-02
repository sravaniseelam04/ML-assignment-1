#creating an empty dictonary called dog.
dog ={}
#Adding name, color, breed, legs, age to the dog dictionary.
dog.update({ "name"  : "holy" , "color" : "brown","breed" : "poodle","ages" : " 4 years","legs" :  " 4 legs"})
print(dog)

#Create a student dictionary and add first_name, last_name, gender, age, marital status,
#skills, country, city and address as keys for the dictionary.
student = {"first_name": "sravani", "last_name":"seelam", "gender":"female", "age":"23", "marital status":"single",
"skills": ['python', 'java', 'c++'], "country":"india", "city":"khammam", "address":"PNR duplex, telangana, 507002"}

#length of the student dictionary
print( "the lenght of the student dictonary :", len(student))

#Get the value of skills and check the data type.
print("the updated skills are:",student["skills"])
print("the datatype of the skills:",type(student["skills"]))

#Modify the skills values by adding one or two skills
student["skills"].append(".net")
print("the modified skill set",student["skills"])

#Get the dictionary keys as a list
keys =  student.keys()
print(keys)

#Get the dictionary values as a list
values =  student.values()
print(values)