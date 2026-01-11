#Write a program to input 2 numers and print their sum
"""a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
sum=a+b
print(sum)"""


#write a program to input side of square and prints it's area

"""a=float(input("Enter the side of the square:"))
A=a*a
print("Area=",A)"""

#Write a program to input 2 floating point values and print their average

"""x=float(input("Enter first number:"))
y=float(input("Enter second number:"))
avg=(x+y)/2
print("Average=",avg)"""


#Write a program to input 2 numbers a and b. Print true if a is greater than or equal to b.If not print false

"""a=float(input("Enter first number:"))
b=float(input("Enter second number:"))
if(a>=b):
    print("True")
else:
    print("False")"""


#Write a program to input user first name and print it's length
"""
name="Chethan$PS$"
print(len(name))
print(name.count("$"))"""


#Write a program to check if a number entered by the user is odd or even
"""
n=int(input("Enter a number:"))
if(n%2==0):
    print("Even number!")
else:
    print("Odd number!")"""

#Write a program to find greatest of three numbers entered by the user
"""
n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))
n3=int(input("Enter third number:"))
if(n1>n2 and n1>n3):
    print("The greater number is :",n1)
elif(n2>n1 and n2>n3):
    print("The greater number is:",n2)
else:
    print("The greater number is :",n3)"""

#Write a program to check if a number is multiple of 7 or not.
"""
n=int(input("Enter a number:"))
if(n%7==0):
    print("It is a multiple of 7!")
else:
    print("It is not a multiple of 7!")"""

#Write a program to ask users to enter name of their 3 favourite movies and store them in a list
"""
print("Enter your three favourite movies")
m1=input("Enter 1st movie:")
m2=input("Enter 2nd movie:")
m3=input("Enter 3rd movie:")
lst=[m1,m2,m3]
print(lst)"""

#Write a program to check if a list contains palindrome of elements
"""
lst=[1,2,3,4,1]
if(lst==lst[::-1]):
    print("palindrome!")
else:
    print("Not palindrome!")"""

"""Write a program to count number of students with "A" grade in the following tuple
("C","D","A","A","B","B","A")
store the above values in a list and sort them from "A" to "D"
"""

tup=("C","D","A","A","B","B","A")
print("Total number of students with Grade A is:",tup.count("A"))

grade_list=list(tup)
grade_list.sort()
print("Sorted list:",grade_list)

    

