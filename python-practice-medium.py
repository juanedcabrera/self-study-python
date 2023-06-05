# 1. Write a python program to find the second largest number in a list
def second_largest(x):
    x.sort()
    # Negative numbers will start from the end of the list
    return x[-2]
print(second_largest([1,2,3,4,5]))

# 2. Write a Python program to remove all duplicates from a given list
def remove_duplicates(x):
    # Set will remove duplicates because it only takes unique values. Then you convert it back to a list.
    return list(set(x))
print(remove_duplicates([1,2,3,4,5,5,5,5,5,5,5,5,5,5,5]))

# 3. Write a python program to sort a list of tuples based on the second element of each tuple.
def sort_tuples(x):
    # This will sort the list based on the second element of each tuple
    # The sorted function will return a new list. It will not change the original list and it will sort the list in ascending order.
    # The sort function uses a key argument to specify a function to be called on each list element prior to making comparisons.
    # The lambda function takes the x value and returns the second element x[1] of each tuple, which is the second element of each tuple.
    # [1] is the index of the second element of each tuple.
    return sorted(x, key=lambda x: x[1])
print(sort_tuples([(2,1),(21,6),(12,11),(45,3)]))

# 4. Write a python function that takes a list of words and returns the longest word in the list
def longest_word(x):
    # Set the first word in the list as the longest word
    longest = x[0]
    # Loop through the list
    for word in x:
        # If the length of the current word is greater than the length of the longest word
        if len(word) > len(longest):
            # Set the current word as the longest word
            longest = word
    return longest
print(longest_word(['hello','world1','my','name','is','sammy']))

# 5. Write a python program to generate a random password of a given liength, consisting of upper case letters, lower case letters, numbers, and symbols.
# Random and String are modules that comes with python's library. Random will generate random numbers and String will generate random strings.
import random
import string
def random_password(length):
    # Create a variable to store the password
    password = ''
    # Create a variable to store the characters that will be used to generate the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Loop through the length of the password
    for i in range(length):
        # Add a random character to the password
        password += random.choice(characters)
    return password
print(random_password(10))
# Taking it a step further. You can specify the amount of digits, letters, and symbols you want in the password.
def random_password2(length, num_letters, num_digits, num_symbols):
    # Create a variable to store the password
    password = ''
    # Create a variable to store the characters that will be used to generate the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Loop through the length of the password
    for i in range(num_letters):
        # Add a random character to the password
        password += random.choice(string.ascii_letters)
    for i in range(num_digits):
        # Add a random character to the password
        password += random.choice(string.digits)
    for i in range(num_symbols):
        # Add a random character to the password
        password += random.choice(string.punctuation)
    # Create a list of the password
    password_list = list(password)
    # Shuffle the list
    random.shuffle(password_list)
    # Join the list back together
    password = ''.join(password_list)
    return password
# 6. Write a python program to find the sum of the digits of a given number
def sum_digits(x):
    # Convert the number to a string
    # It needs to be a string because you can't loop through a number. It will still understand the value of the number.
    x = str(x)
    # Create a variable to store the sum
    sum = 0
    # Loop through the number
    for i in x:
        # Add each digit to the sum
        sum += int(i)
    return sum
print(sum_digits(12346))

# 7. Write a python program to find the number of words in a sentence.
def num_words(x):
    # Split the sentence into a list of words
    x = x.split()
    # Return the length of the list
    return len(x)
print(num_words('Hello my name is Sammy'))

# 8. Write a python program to reverse a string without using any built-in functions
def reverse_string(x):
    # Create a variable to store the reversed string
    reversed_string = ''
    # Loop through the string
    for i in x:
        # Add each character to the beginning of the reversed string
        reversed_string = i + reversed_string
    return reversed_string
print(reverse_string('Hello World'))

# 9. Write a python program to check if a given string is a pangram or not
# A pangram is a sentence that contains all the letters of the English alphabet at least once.
def pangram(x):
    # Create a variable to store the alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # Loop through the alphabet
    for i in alphabet:
        # If the letter is not in the string
        if i not in x:
            # Return False
            return False
    # Return True
    return True
print(pangram('The quick brown fox jumps over the lazy dog'))

# 10. Write a python program to find the common elements between two lists
def common_elements(x, y):
    # Create a variable to store the common elements
    common = []
    # Loop through the first list
    for i in x:
        # If the element is in the second list
        if i in y:
            # Add the element to the common list
            common.append(i)
    return common
print(common_elements([1,2,3,8,9], [1,2,3,4,5,6,7,8,9]))
