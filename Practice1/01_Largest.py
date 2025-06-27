# To find largest of 3 numbers
 
# 1.By using the if_else condition

# a,b,c=10,20,199
# if a>=b and a>=c:
#     print("Largest:",a)
# elif b>=a and b>=c:
#     print("Largest:",b)
# else:
#     print("Largest:", c)


# 2.By using the built in function max()

# a,b,c=20,306,45
# print("Largest:",max(a,b,c))


# 3.By using the list

nums=[30,45,77,1,98,67]
nums.sort()
print("Largest:",nums[-1])