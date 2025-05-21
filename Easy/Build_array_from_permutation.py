############################################################################################################################
# Build Array from Permutation:                                                                                            #
# Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for  #
# each 0 <= i < nums.length and return it.                                                                                 #
# A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).                    #
# Follow-up: Can you solve it without using an extra space (i.e., O(1) memory)?                                            #
############################################################################################################################

from typing import List

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        constant = 1001 # Define a constant to encode two values in one
        for i in range(len(nums)):
            a = nums[i] # First I need to check the new index at nums[i]
            b = nums[a] % constant # Here I need to get b from the encode value
            nums[i] = a + b * constant # Finally asigne the encode value
        for i in range(len(nums)):
            nums[i] //= constant # Extract the final int value nums[nums[i]]
        return nums
    


# Test------------------------------------------------------
objeto = Solution()
# Define new test cases for each iteration
test_cases = {
    0: ([0, 2, 1, 5, 3, 4], [0, 1, 2, 4, 5, 3]),
    1: ([5, 0, 1, 2, 3, 4], [4, 5, 0, 1, 2, 3])}

for test_num, (input_data, expected) in test_cases.items():
    # New copy of the input for each test
    current_input = input_data.copy()
    output = objeto.buildArray(current_input)
    if output == expected:
        print(f"Test{test_num}: Accepted")
    else:
        print(f"Test{test_num}: Failed")
    print(f"Output: {output} \nExpected: {expected} \n")