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

s = 'radefce'
t = 'ace'

def subsequence(s,t):
    # I'm putting everything into an ans string, you can tell because of the ''
    ans = ''
    # Starting both the outer loop and the inner loop with 0
    i = j = 0
    
    # While both of these have characters 
    while i < len(s) and j < len(t):
        # If the outer loop matches the inner loop than
        if s[i] == t[j]:
            # Add the outer loop
            ans += s[i]
            # Move both loops to the next character
            i += 1
            j += 1
        # If they don't match
        elif s[i] != t[j]:
            # Move the outer loop up by 1
            i += 1
        else:
            # If not move the inner loop up by 1
            j += 1
    # If my ans string matches s or t than mark true
    print(ans)
    if ans == s or ans == t:
        return True
    else:
        # If not mark false
        return False

result = subsequence(s, t)
print(result)

#######################################################

# REVERSE STRING

# Example 1
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# Example 2
# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

s = ["h","e","l","l","o"]


# def reverse_string(s):
#     return s[::-1]

# print(reverse_string(s))
            

# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         left = 0
#         right = len(s) - 1
#         while left < right:
#             # This will reverse each letter
#             s[left], s[right] = s[right], s[left]
#             left += 1
#             right -= 1
        

#######################################################

# TWO POINTERS

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

# class Solution:
#     def sortedSquares(self, nums: List[int]) -> List[int]:
#         ans = []
#         left = 0
#         right = len(nums) - 1
        
#         while left <= right:
#             if nums[left] < nums[right]:
#                 ans.append(nums[right]**2)
#                 right -= 1
#             else:
#                 ans.append(nums[left]**2)
#                 left -= 1
#             ans.sort()
#         return ans

#######################################################

# SLIDING WINDOW (constraint is sum of the window)
def find_length(nums, k):
    # We'll start at 0
    left = curr = ans = 0
    # Iterate over the input
    for right in range(len(nums)):
        # We'll increment the current window
        curr += nums[right]
        # As long as the string is broken, we'll move to the left and increment left to shrink the window
        while curr > k:
            curr -= nums[left]
            left += 1
        # Once we know the window is no longer breaking the constraint to update the ans
        # Length of the window will be right-left+1 because it is in index
        ans = max(ans, right - left + 1)
    # This will be a number indicating how long the string will be
    return ans

print(find_length([3,1,2,7,4,2,1,1,5], 8))

#######################################################

# SLIDING WINDOW (constraint to contain at most is one 0)
def find_length2(s):
    left = curr = ans = 0
    for right in range(len(s)):
        if s[right] == "0":
            curr += 1
        while curr > 1:
            if s[left] == "0":
                curr -= 1
            left += 1
        ans = max(ans, right - left + 1)
    return ans

print(find_length2("11001011"))
