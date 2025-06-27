# To find whether a given string is palindrome or not

# 1.Reverse and then compare

# s="madam"
# print("Palindrome" if s==s[::-1] else "Not palindrome")

# 2.Using function

def is_palindrome(s):
    return "Palindrome" if s==s[::-1] else "Not Palindrome"

print(is_palindrome("madam"))