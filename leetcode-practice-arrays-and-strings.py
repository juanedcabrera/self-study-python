# # TWO POINTERS
# # Example 1: Given a string s, return true if it is a palindrome, false otherwise.

# # This function checks if a string is a palindrome using a Two-Pointer approach.
# # This is going to give a Boolean TRUE or FALSE
# def check_if_palindrome(s):
#     # The left pointer starts at the beginning of the string (index 0)
#     left = 0
#     # The right pointer starts at the end of the string (index len(s) - 1)
#     # We must reduce by 1 because Python is a 0 index language
#     right = len(s) - 1
#     # This is a while loop that first checks if left is less than right
#     while left < right:
#         # This is checking if the left indice DOES NOT match the right indice - signaled by the bang = sign
#         # Indice is noted here by the brackets
#         if s[left] != s[right]:
#             # If it doesnt match than it is returning a boolean FALSE
#             return False
#         # Move the pointers closer to the middle
#         left += 1
#         right -= 1
#     # If they all match than it should return True because it is a palindrome
#     return True

# # Call the function and assign the result to a variable
# result = check_if_palindrome('racecar')
# # Print the variable
# print(result)

# #######################################################

# # TWO POINTERS
# # Example 2: Given a sorted array of unique integers and a target integer, return true if there exists a pair of numbers that sum to target, false otherwise.

# nums = [1, 2, 4, 6, 7, 8, 9, 14, 15]
# target = 13

# def check_target(nums, target):
#     # 
#     left = 0
#     right = len(nums) - 1
#     while left < right:
#         current_sum = nums[left] + nums[right]
#         if current_sum == target:
#             return True
#         elif current_sum < target:
#             left += 1
#         else:
#             right -=1
#     return False
# result = check_target(nums, target)
# print(result)

# #######################################################

# # TWO POINTERS
# # Example 3: Given two sorted integer arrays arr1 and arr2, return a new array that combines both of them and is also sorted.

# arr1 = [1,4,7, 10, 15, 20]
# arr2 = [3,5,6]

# # arr1 and arr2 are called "parameters"
# def combine(arr1, arr2):
#     ans = []
#     i = j = 0
#     while i < len(arr1) and j < len(arr2):
#         if arr1[i] < arr2[j]:
#             ans.append(arr1[i])
#             i+=1
#         else:
#             ans.append(arr2[j])
#             j+=1
#     while i < len(arr1):
#         ans.append(arr1[i])
#         i+=1
#     while j < len(arr2):
#         ans.append(arr2[j])
#         j+=1
#     return ans

# result = combine(arr1,arr2)
# print(result)

# #######################################################

# # TWO POINTERS
# # Example 4: Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# # A subsequence of a string is a sequence of characters that can be obtained by deleting some (or none) of the characters from the original string, while maintaining the relative order of the remaining characters. For example, "ace" is a subsequence of "abcde" while "aec" is not.

# s = 'radefce'
# t = 'ace'

# def subsequence(s,t):
#     # I'm putting everything into an ans string, you can tell because of the ''
#     ans = ''
#     # Starting both the outer loop and the inner loop with 0
#     i = j = 0
    
#     # While both of these have characters 
#     while i < len(s) and j < len(t):
#         # If the outer loop matches the inner loop than
#         if s[i] == t[j]:
#             # Add the outer loop
#             ans += s[i]
#             # Move both loops to the next character
#             i += 1
#             j += 1
#         # If they don't match
#         elif s[i] != t[j]:
#             # Move the outer loop up by 1
#             i += 1
#         else:
#             # If not move the inner loop up by 1
#             j += 1
#     # If my ans string matches s or t than mark true
#     print(ans)
#     if ans == s or ans == t:
#         return True
#     else:
#         # If not mark false
#         return False

# result = subsequence(s, t)
# print(result)

# #######################################################

# # REVERSE STRING

# # Example 1
# # Input: s = ["h","e","l","l","o"]
# # Output: ["o","l","l","e","h"]

# # Example 2
# # Input: s = ["H","a","n","n","a","h"]
# # Output: ["h","a","n","n","a","H"]

# s = ["h","e","l","l","o"]


# # def reverse_string(s):
# #     return s[::-1]

# # print(reverse_string(s))
            

# # class Solution:
# #     def reverseString(self, s: List[str]) -> None:
# #         left = 0
# #         right = len(s) - 1
# #         while left < right:
# #             # This will reverse each letter
# #             s[left], s[right] = s[right], s[left]
# #             left += 1
# #             right -= 1
        

# #######################################################

# # TWO POINTERS

# # Input: nums = [-4,-1,0,3,10]
# # Output: [0,1,9,16,100]
# # Explanation: After squaring, the array becomes [16,1,0,9,100].
# # After sorting, it becomes [0,1,9,16,100].

# # class Solution:
# #     def sortedSquares(self, nums: List[int]) -> List[int]:
# #         ans = []
# #         left = 0
# #         right = len(nums) - 1
        
# #         while left <= right:
# #             if nums[left] < nums[right]:
# #                 ans.append(nums[right]**2)
# #                 right -= 1
# #             else:
# #                 ans.append(nums[left]**2)
# #                 left -= 1
# #             ans.sort()
# #         return ans

# #######################################################

# # SLIDING WINDOW (constraint is sum of the window)
# def find_length(nums, k):
#     # We'll start at 0
#     left = curr = ans = 0
#     # Iterate over the input
#     for right in range(len(nums)):
#         # We'll increment the current window
#         curr += nums[right]
#         # As long as the string is broken, we'll move to the left and increment left to shrink the window
#         while curr > k:
#             curr -= nums[left]
#             left += 1
#         # Once we know the window is no longer breaking the constraint to update the ans
#         # Length of the window will be right-left+1 because it is in index
#         ans = max(ans, right - left + 1)
#     # This will be a number indicating how long the string will be
#     return ans

# print(find_length([3,1,2,7,4,2,1,1,5], 8))

# #######################################################

# # SLIDING WINDOW (constraint to contain at most is one 0)
# def find_length2(s):
#     left = curr = ans = 0
#     for right in range(len(s)):
#         if s[right] == "0":
#             curr += 1
#         while curr > 1:
#             if s[left] == "0":
#                 curr -= 1
#             left += 1
#         ans = max(ans, right - left + 1)
#     return ans

# print(find_length2("11001011"))

# #######################################################

# # SLIDING WINDOW (constraint must greater than 1)


# class Solution:
#     def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
#         if k <= 1:
#             return 0
#         ans = left = 0
#         curr = 1
#         for right in range(len(nums)):
#             curr *= nums[right]
#             while curr >= k:
#                 curr //= nums[left]
#                 left += 1
#             ans += right - left + 1
#         return ans

# nums = [10, 5, 2, 6]
# k = 100

# solution = Solution()
# print(solution.numSubarrayProductLessThanK(nums, k))

# ########################
# # Sliding Window - Maximum Average Subarray

# class Solution:
#     def findMaxAverage(self, nums: list[int], k: int) -> float:
#         # current is the sum of the first k elements
#         current = sum(nums[:k])
#         # ans is the where we will store the the highest sum
#         ans = current
#         # iterate over the rest of the elements
#         for i in range(k, len(nums)):
#             # add the current element and subtract the first element of the window
#             current += nums[i] - nums[i-k]
#             # update the ans if the current average is greater
#             ans = max(ans, current)
#         # return the average
#         return ans / k
    
# # Note: current += nums[i] - nums[i-k] updates the current sum. It adds the current element nums[i] and subtracts the element at i - k position. This effectively removes the leftmost element that is no longer part of the current subarray and adds the new rightmost element.

# # For example, let's say k = 3 and we have nums = [1, 2, 3, 4, 5]. Initially, current is the sum of the first three elements, i.e., current = 1 + 2 + 3 = 6. In the first iteration, i = 3, so we subtract nums[0] (the leftmost element of the previous subarray) and add nums[3] (the rightmost element of the current subarray). Thus, current becomes 6 - 1 + 4 = 9, representing the sum of the subarray [2, 3, 4]. This sliding window approach allows us to efficiently update the sum without recomputing it from scratch at each iteration.

# ########################

# class Solution:
#     def longestOnes(self, nums: list[int], k:int) -> int:
#         # Dynamic Sliding Window
#         left = right = 0
#         # Iterate over the nums list range(len(nums))
#         for i in range(len(nums)):
#             print("R", right)
#             print("L", left)
#             # if the current indice value is 0
#             if nums[i] == 0:
#                 #  decrement k
#                 k-=1
#             # if k is less than 0
#             if k < 0:
#                 if nums[left] == 0:
#                     # increment k
#                     k+=1
#                 # increment left
#                 left += 1
#             # increment right
#             right += 1
#         # return right - left which is the length of the window
#         return right - left 

# solution = Solution()

# # nums = [1,1,1,0,0,0,1,1,1,1,0]
# # k = 2

# # R 0
# # L 0
# # R 1
# # L 0
# # R 2
# # L 0
# # R 3
# # L 0
# # R 4
# # L 0
# # R 5
# # L 0
# # R 6
# # L 1
# # R 7
# # L 2
# # R 8
# # L 3
# # R 9
# # L 4
# # R 10
# # L 4
# # Ans = 6

# ########################

# # Given a sorted array of unique integers and a target integer, return true if there exists a pair of numbers that sum to target, false otherwise.

# nums = [1, 2, 4, 6, 7, 8, 9, 14, 15]
# target = 45

# def check_target_num(nums: list, target: int) -> bool:
#     left = 0
#     right = len(nums) - 1

#     while left < right:
#         current_sum = nums[left] + nums[right]
#         if current_sum == target:
#             return True
#         elif current_sum < target: 
#             left += 1
#         else:
#             right -= 1
#     return False
# result = check_target_num(nums, target)
    


# Given a string s, return true if it is a palindrome, false otherwise.

# def check_if_palindrome(s: str):
#     left=0
#     right=len(s)-1

#     while left < right:
#         if s[left] != s[right]:
#             return False
#         else:
#             left+=1
#             right-=1
#     return True


# result = check_if_palindrome('racecar')
# print(result)

# nums = [1, 2, 4, 6, 7, 8, 9, 14, 15]
# target = 43

# def target_bool(nums:list, target:int) -> bool:
#     left = 0
#     right = len(nums) - 1

#     while left < right:
#         current_sum = nums[left] + nums[right]
#         if current_sum == target:
#             return True
#         elif current_sum < target:
#             left+=1
#         else:
#             right-=1
#     return False
# result = target_bool(nums, target)
# print(result)

# arr1 = [1,3,5,9,10]
# arr2 = [2,4,6,7]

# def combined_array(arr1: list, arr2: list) -> list:
#     ans = []
#     i=j=0

#     while i < len(arr1) and j < len(arr2):
#         if arr1[i] < arr2[j]:
#             ans.append(arr1[i])
#             i+=1
#         else:
#             ans.append(arr2[j])
#             j+=1
#     if i < len(arr1):
#         ans.append(arr1[i])
#         i+=1
#     if j < len(arr2):
#         ans.append(arr2[j])
#         j+=1
#     return ans
# result = combined_array(arr1, arr2)
# print(result)

# nums = [1, 2, 4, 6, 7, 8, 9, 14, 15]
# target = 19

# def sum_to_target(nums:list, target:int) -> bool:
#     left = 0
#     right = len(nums) - 1

#     while left < right:
#         current_sum = nums[left] + nums[right]
#         if current_sum == target:
#             return True
#         elif current_sum < target:
#             left += 1
#         else:
#             right -= 1
#     return False

# result = sum_to_target(nums, target)
# print('This is the result of sum-to-target',result)

# s = ['a','b','c','d','e']
# t = ['a','c','e']

# def subsequence(s:list, t:list) -> bool:
#     ans = []
#     i=j=0
#     while i < len(s) and j < len(t):
#         if s[i] == t[j]:
#             ans.append(s[i])
#             i+=1
#             j+=1
#         elif s[i] != t[j]:
#             i+=1
#         else:
#             j+=1
#     if ans == s or ans == t:
#         return True
#     return False

# result = subsequence(s,t)
# print('this is subsequence ', result)

# s = ["h","e","l","l","o"]

# class Solution:

# solution = Solution.reversed_string(s)
# print(s)



# from itertools import zip_longest


# word1 = "abc" 
# word2 = "pqr"

# def merged_string(word1 = str, word2 = str) -> str:
#     merged=""
#     i = j = 0
#     while i < len(word1) and j < len(word2) :
#         merged += word1[i]
#         merged += word2[j]
#         i+=1
#         j+=1
#     if i < len(word1):
#         merged += word1[i]
#     if j < len(word2):
#         merged += word2[j]
#     return merged

# result = merged_string(word1, word2)

# print(result)

# def merged_alternate(word1: str = "", word2: str = "") -> str:
#     merged = ""
#     for word1, word2 in zip_longest(word1, word2, fillvalue=""):
#         merged+=word1+word2
#     return merged

# result = merged_alternate(word1,word2)
# print(result)