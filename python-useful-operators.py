# mylist = [1, 2, 3]
# for num in range(10):
#     print('This will print the range of numbers', num, 'but not including 10')

# index_count = 0
# word = 'abcde'
# for letter in word:
#     print('At index {} the letter is {}'.format(index_count, letter))
#     index_count += 1

# # enumerate() function
# word = 'abcde'
# for item in enumerate(word):
#     print('This will print the index and the letter', item)

# zip() function
# mylist1 = [1, 2, 3]
# mylist2 = ['a', 'b', 'c']
# mylist3 = [100, 200, 300]
# for item in zip(mylist1, mylist2, mylist3):
#     print('This will print the zipped lists', item)

# output = 'x' in ['x', 'y', 'z']
# print('This will print the boolean value of x in the list', output)

# from random import shuffle
# mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# shuffle(mylist)
# print('This will print the shuffled list', mylist)

# from random import randint
# randint(0, 100)
# print('This will print a random integer between 0 and 100', randint(0, 100))

# result = input('Enter a number here: ')
# print('This will print the result of the input', result)
# input() always returns a string
# result = int(input('Enter a number here: ')) # this will convert the input to an integer

# mylist = [x for x in 'word']
# print('This will print the list', mylist)

# mylist = [num**2 for num in range(0, 11)]
# print('This will print the list of numbers squared', mylist)

# celcius = [0, 10, 20, 34.5]
# fahrenheit = [((9/5)*temp + 32) for temp in celcius]
# print('This will print the list of celcius converted to fahrenheit', fahrenheit)