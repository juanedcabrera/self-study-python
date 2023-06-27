# # Iterating over a sequence
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)

# dogs = ["French Bulldog", "Mastiff", "Rottweiler"]
# for dog in dogs:
#     print(dog)

# kids = ["Sofia", "Lucas", "Jack"]
# for kid in kids:
#     print(kid)

# friends = ["Ryan", "Andrew", "Cody", "Taylor"]
# for friend in friends:
#     print(friend)

# # For Each Loops
# fruits = ["apple", "banana", "cherry"]
# for index, fruit in enumerate(fruits):
#     print(f"Index: {index}, Fruit: {fruit}")

# dogs = ["French Bulldog", "Mastiff", "Rottweiler"]
# for index, dog in enumerate(dogs):
#     print(f"Index: ", {index}, 'Dog: ', {dog})

# # Talking point: I'm defining a list called kids
# # Enumerate keeps a count of iterations
# kids = ["Sofia", "Lucas", "Jack"]
# for index, kid in enumerate(kids):
#     print(f"Index: {index}, Kid: {kid}")

# While Loops

# count = 1
# while count <=  5:
#     print(count)
#     count += 1

# count = 5
# while count <= 10:
#     print(count)
#     count += 1

# Nested For Loop
for i in range (1,4):
    for j in range(1, i+1):
        print("*", end="")
    print()
# There is an outer loop that is iterating and an inner loop that iterates based on the current value of i