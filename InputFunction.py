# ****************************Input function in python********************************* 

a = input() 
print(a) 

a = input() 
print(a+a)

a = input() 
print(int(a)+int(a)) 
# input function always reads input value as a string

name = input("Enter your name: ")
print(f"Welcome {name}")

age = input("Enter your age: ")
# print(f"Ohh you're just {age}!")
print(f"So next year you will be {int(age)+1}!")  

# multple input from user 
# input from user to add two number and print result
x = input("Enter first number: ")
y = input("Enter second number: ") 
print(f"Sum of {x} & {y} is {int(x) + int(y)}")
