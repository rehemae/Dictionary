# #  1: Convert two lists into a dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
number={}
for s in keys:
 for x in values:
     number[s]=x
print(number) 

# #  Merge two Python dictionaries into one
 
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict3={**dict1, **dict2}
print(dict3)

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict1.update(dict2)
print(dict1)


# Check if a key exists in a dictionary
dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
for key in dict:
    print(key)
 #  Check if a value exists in a dictionary
sampleDict = {"class": {"student": {"name": "Mike", "marks": {"physics": 70, "history": 80 } } }}
for value in sampleDict:
    print(value)

#Merge two dictionaries
person = {"name": "Jessa", 'country': "USA", "telephone": 1178}
Dict = {"class": {"student": {"name": "Mike", "marks": {"physics": 70, "history": 80 } } }}
person.update(Dict)
print(person)


# Joining three dictionaries
student_dict1 = {'Aadya': 1, 'Arul': 2, }
student_dict2 = {'Harry': 5, 'Olivia': 6}
student_dict3 = {'Nancy': 7, 'Perry': 9}
student_dict={**student_dict1, **student_dict2, **student_dict3}
print(student_dict)
print(student_dict1|student_dict2|student_dict3)

# To find the even  square number
numbers = [1, 3, 5, 2, 8]
even_squares = {x: x ** 2 for x in numbers if x % 2 == 0}
print(even_squares)

# To remove one key in the dictionary

name={"rehema":22,"anna":222,"Asha":11,"Grace":11,"Amina":11}
name.pop("rehema")
print(name)





