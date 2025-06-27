# Check if number is odd or even

# 1.By using modular operator

# n=12
# print("Even" if n%2==0 else "odd")


# 2.By using function and input

def check_even_odd(n):
    return "Even" if n%2==0 else "odd"

n=int(input("Enter number:"))
print(check_even_odd(n))