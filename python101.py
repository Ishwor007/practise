#!/usr/bin/python3

#print string
print("hello")
print('hello')
print("""hello
how are you""")

#math
print("Math time:")
print(50+50) #add
print(50-50) #substract
print(50 ** 2) #exponent

#variable and method
print("Fun with variable and method")
quote = "Everything is fair in love and war"
print(quote)
print(len(quote))
print(quote.upper())
print(quote.lower())
print(quote.title())

name = "seetal"
age=20.06
print(int(age))
print("my name is " + name + " and i am " + str(int(age)) +" years old")
print("\n")


#function
print("Example of function")
def intro():
	name="seetal"
	age=20
	print("my name is " + name + " and i am " + str(int(age)) +" years old")

intro()

def add(x,y):
	return x+y
print(add(7,7))

#conditional statement
print("conditional statement")
def check(num):
	if(num>2):
		return "you are in if"
	elif(num==2):
		return "you are in else if"
	else:
		return "you are in else"
print(check(1))
print(check(2))
print(check(3))


print("\n")
#List
print("lists")
movies=["one","two","three","four","five","six"]
print(movies)
print("\n")
print(movies[0])
print(movies[0:3])
print(movies[0:])#not end all
print("\n")
movies.append("seven")
print(movies)
movies.pop()#last will remove
movies.pop(1)

print("\n")
movies=["one","two","three","four","five","six"]
person=["seetal","sneha","manju","narayan"]
combined = zip(person,movies)
print(list(combined))


#Tuples #cannot pop append
print("\n")
print("Tuples")
grades = ("A","B","C","D")
print(grades[1])

#looping
print("For loops")
  

vegetables = ['cucumber','spinach','ladyfinger']
for x in vegetables:
	print(x);

print("while loop")
i=1
while i < 10:
	print(i)
	i+=1


print("extra added for git practise")

























































