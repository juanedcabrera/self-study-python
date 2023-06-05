# 1. Write a python program to print "Hello, World!" on the console
print('Hello, World!')
# 2. Write a python program to add two numbers and print their return
def add_two_numbers(x,y):
    return x + y
print(add_two_numbers(1,2))
# 3. Write a python program to check if a given number is even or odd
def even_or_odd(x):
    if x % 2 == 0:
        return 'Even'
    else:
        return 'Odd'
print(even_or_odd(2))
# 4. Write a python program to find the largest number among three given numbers
def largest_number(x,y,z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    else:
        return z
print(largest_number(1,2,3))
# 5. Write a python program to calculate the factorial of a given number
# def factorial(x):
#     if x == 0:
#         return 1
#     else:
#         return x * factorial(x-1)
# print(factorial(4))
# This is using recursion. Recursion is when a function calls itself.
def factorial(x):
    # This is where we will store the result with the initial value of 1. And then we will multiply it by i.
    result = 1
    # This is the for loop. It will start at 1 and go up to x+1 so that it will include x.
    for i in range(1, x+1):
        # This is the result. It will multiply the result by i.
        result *= i
    return result
print (factorial(4))
# This will print the factorial of 4, which is 24. 1*1 = 1, 1*2 = 2, 2*3 = 6, 6*4 = 24.
# The last number is the number that you want to find the factorial of
# 6. Write a Python program to check if a given string is a palindrome or not
def palindrome(x):
    # This will reverse the string
    if x == x[::-1]:
        # This will check if the string is the same as the reversed string
        return True
    else:
        return False
print(palindrome('racecar'))
# 7. Write a Python program to count the number of vowels in a given string
def count_vowels(x):
    count = 0
    # This is the for loop. It will go through each letter in the string.
    for i in x:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            # This will check if the letter is a vowel
            count += 1
    return count
print(count_vowels('hello'))
# # Another way to do this is:
# def count_vowels(x):
#     count = 0
#     # This is the for loop. It will go through each letter in the string.
#     for i in x:
#         if i in 'aeiou':
#             # This will check if the letter is a vowel
#             count += 1
#     return count
# print(count_vowels('hello'))
# 8. Write a Python program to find the length of a list
def length_of_list(x):
    count = 0
    # This is the for loop. It will go through each item in the list.
    for i in x:
        count += 1
    return count
print(length_of_list([1,2,3,4,5]))
# # Another way to do this is:
# def length_of_list(x):
#     return len(x)
# print(length_of_list([1,2,3,4,5]))
# 9. Write a python program to reverse a given list
def reverse_list(x):
    return x[::-1]
print(reverse_list([1,2,3,4,5]))
# # Another way to do this is:
# def reverse_list(x):
#     x.reverse()
#     return x
# print(reverse_list([1,2,3,4,5]))
# 10. Write a python program to check if a given number is prime
# A prime number is a number that is only divisible by 1 and itself.
# The formula for a prime number is n % i == 0
def prime_number(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
print(prime_number(7))