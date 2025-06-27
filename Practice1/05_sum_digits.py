# Sum of digits of a number

# 1.Using loop and modulus

# n=int(input("Enter number:"))
# sum=0
# while n:
#     sum+=n%10
#     n=n//10
# print(sum)


# 2.Convert to string

# n=123
# print(sum(int(d) for d in str(n)))


# 3.By using recursion

def sum_digits(n):
    return 0 if n==0 else n%10+sum_digits(n//10)

print(sum_digits(1999))