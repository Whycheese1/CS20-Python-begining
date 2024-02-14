#Attributes
hair_color = "brown"
eye_color = "brown"
name = "Jarrett" #String
age = 16 #Integer
height = 6.1 #Float
hungry = True #Boolean

#conditional statement
print(hungry)

if hungry:
    print("Take these six hamburgers!")
else:
    print("Take this water")
    
if hungry == True:
    print("Take these five hamburgers!")
else:
    print("Take this water")
    
#variabe = True Statement if (condition) else False statement
state = "hamburgers" if hungry else "Water"
print(state)

#Data Types
print("Hair Color: " + str(type(hair_color)) )
print("Eye Color: " + str(type(eye_color)) )
print("Name: " + str(type(name)) )
print("Age: " + str(type(age)) )
print("height: " + str(type(height)) )
print( type(hungry) )