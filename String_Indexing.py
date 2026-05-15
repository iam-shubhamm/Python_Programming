#************************************** String Indexing*****************************************

# strings- chars in single, double and triple quotes
name = "Shubham"     # creating a string
print(name)

print(type(name))   # checking data type

print("It's easy")
print("Hello World")

print(''' "kw-double Quotes" ''') 

print(" \"kw-double Quotes\" ") 

# Formatted Strings - insert variables or experssions
# 1. Old style formatting - % operator 

name = "Shubham"
age = 23
print("My name is %s and I'm %d" % (name, age)) 
# %s, %d are placeholders for the string and int 


#2. str.format() method 

name = "Shubham"
age = 23 
print("My name is {} and I'm {}".format(name, age)) 


# you can reference variables by index or keyword
print("My name is {0} and I'm {1}".format(name, age))
print("My name is {1} and I'm {0}".format(name, age))

print("My name is {name} and I'm {age}".format(name="Keshav", age="21"))

#3. f-strings 

name = "Singh"
age = 23
print(f"My name is {name} and I'm {age}")

print(f"My age after 5 years will be {age + 5}") 


# Escape Characters - backslash with chars 
print(''' "kw-double Quotes" ''') 

print(" \"kw-double Quotes\" ")  # double quotes using \

print(" \'kw-single Quotes\' ") # single quote using \

print("Hello\nWorld")       # new line
print("Hello\tWorld")       # tab - space 

# String Operators in Python 
a = "Hello"
b = "Python"

print(a+b)      # concatenate 
print(a*2)      # multiple copies 
# [] - slice, [:] - range  -- scroll below

if "h" in a:
    print("Yess")
else:
    print("noo")

    
if "h" not in a:
    print("Yess")
else:
    print("noo") 

print(r"Hello\nWorld")  # Raw string: suppress the escape chars 


# String Indexing

my_name = "Shubham"
# index:   012345

print(my_name[0])       # first character of str 
print(my_name[1])       # second character of str 
print(my_name[2])       # third character of str 
print(my_name[3])       # fourth character of str 
print(my_name[4])       # fifth character of str 
print(my_name[5])       # sixth character of str 
print(my_name[-1]) 

name2   =  "Hello World"
# index:    012345678910
# -ve index:1110987654321 -
print(name2[5])     # blank space is also a char
print(name2[-1])    # last char from str
print(name2[-3])    # 3rd last char from str 



