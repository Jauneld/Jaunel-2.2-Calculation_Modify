#Jaunel Deans 
#September 29, 2023
# I modified the code to make it more personalized to the user and that it and add and mulitply numbers that are given to it. 

# Starter code

name = input("Hello user. What is your name? ") #assigned variable name to hold the value of what the user will input as they answer the question 
program = input(name + " is a really nice name. Do you like programming? ") #I used the value of name to address the user and ask them for another input. the value will be assigned to the variable program. 
print(name, "you answered" , program + ". Thanks for your response.")#I used a print statement to print the user's name and answer. 

num1 = 10
print("Enter number: ")
num2 = int(input()) #Added the int() to turn the string to a interger

total1 = num1 + num2
product2 = num1*num2 #add variable fro multiplication

print(name , str(num1) + " plus " + str(num2) + " = " , str(total1) + ". Also you said" , program , "to programming") #added total1 to the output statement and the response to the programming question. 
print(name , str(num1) + " times " + str(num2) + " = " , str(product2)+ ". Also you said" , program , "to programming")

# Instructions

# Line 4 creates an error. Look carefully to see what is wrong with the code and fix it.
## input will be taken as a string so the calculations will not work. 

# Add a text prompt between lines 3 and 4 to tell the user to enter a number.
## print("Enter number: ") will prompt the user to enter a number. 

# Complete line 8 to concatenate total 1 into the output statement.
## , str(total1)

# Add a new variable with a sensible identifier.  Multiply num1 and num2 together and assign the result into this variable.
## quotient2 = numl*num2

# Output num1, num2 and your new variable in a similar format to line 8.
##print(str(num1) + " times " + str(num2) + " = " , str(product2))