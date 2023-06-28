# TWO POINTERS
# Example 1: Given a string s, return true if it is a palindrome, false otherwise.

# This function checks if a string is a palindrome using a Two-Pointer approach.
# This is going to give a Boolean TRUE or FALSE
def check_if_palindrome(s):
    # The left pointer starts at the beginning of the string (index 0)
    left = 0
    # The right pointer starts at the end of the string (index len(s) - 1)
    # We must reduce by 1 because Python is a 0 index language
    right = len(s) - 1
    # This is a while loop that first checks if left is less than right
    while left < right:
        # This is checking if the left indice DOES NOT match the right indice - signaled by the bang = sign
        # Indice is noted here by the brackets
        if s[left] != s[right]:
            # If it doesnt match than it is returning a boolean FALSE
            return False
        # Move the pointers closer to the middle
        left += 1
        right -= 1
    # If they all match than it should return True because it is a palindrome
    return True

# Call the function and assign the result to a variable
result = check_if_palindrome('racecar')
# Print the variable
print(result)

#######################################################

# TWO POINTERS
# Example 2: Given a sorted array of unique integers and a target integer, return true if there exists a pair of numbers that sum to target, false otherwise.

nums = [1, 2, 4, 6, 7, 8, 9, 14, 15]
target = 13

def check_target(nums, target):
    # 
    left = 0
    right = len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return True
        elif current_sum < target:
            left += 1
        else:
            right -=1
    return False
result = check_target(nums, target)
print(result)

#######################################################

# TWO POINTERS
# Example 3: Given two sorted integer arrays arr1 and arr2, return a new array that combines both of them and is also sorted.

arr1 = [1,4,7, 10, 15, 20]
arr2 = [3,5,6]

# arr1 and arr2 are called "parameters"
def combine(arr1, arr2):
    ans = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])
            i+=1
        else:
            ans.append(arr2[j])
            j+=1
    while i < len(arr1):
        ans.append(arr1[i])
        i+=1
    while j < len(arr2):
        ans.append(arr2[j])
        j+=1
    return ans

result = combine(arr1,arr2)
print(result)

#######################################################

# TWO POINTERS
# Example 4: Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a sequence of characters that can be obtained by deleting some (or none) of the characters from the original string, while maintaining the relative order of the remaining characters. For example, "ace" is a subsequence of "abcde" while "aec" is not.

s = 'abcde'
t = 'ace'

def subsequence(s,t):
    ans = ''
    i = j = 0
    
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            ans += s[i]
            i += 1
            j += 1
        elif s[i] != t[j]:
            i += 1
        else:
            j += 1
    if ans == s or ans == t:
        return True
    else:
        return False

result = subsequence(s, t)
print(result)