# To find the factorial of a given number

# 1.By using the loop 

# n=int(input("Enter a number:"))
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(fact)

# 2.By using recusrion

# def factorial(n):
#     return 1 if n==0 else n*factorial(n-1)

# print(factorial(7))


# 3.By using math.factorial()

import math
print(math.factorial(3))