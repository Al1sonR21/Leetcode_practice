############################################################################################################################
# Two sum:                                                                                                                 #
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target #
# You may assume that each input would have exactly one solution, and you may not use the same element twice. You can      #
# the answer in any order.                                                                                                 #
# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?                                    #
############################################################################################################################

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
     # Map the numbers in the array with a hash
     elements = {}
     # Iterate the array to compute the complement
     for i in range(len(nums)):
        complement = target - nums[i]
        # Evaluate if the complement is at the array
        if complement in elements:
            return [elements[complement],i] # Return if it id found
        else:
            elements[nums[i]] = i # If it is not almacenated
    

# Test------------------------------------------------------

objeto = Solution()
for i in range(3):
    case = {0: [2, 7, 11, 15], 1: [3,2 , 4], 2: [3,3]}
    targets = {0: 9,  1: 6, 2:6 }
    solutions = {0: [0, 1], 1: [1, 2], 2: [0, 1]}
    if objeto.twoSum(case[i], targets[i]) == solutions[i] :
        print(f"Test{i}: Accepted ")
    else:
         print("Tste + {i}: Failed")
    print(f"Output: {objeto.twoSum(case[i], targets[i])} \nExpected {solutions[i]} \n")
