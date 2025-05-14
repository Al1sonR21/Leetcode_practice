from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Iterates the array
        for i in range(len(nums)):
        # Make other iteration to add element to the list and compare if it is equal to target
            for j in range(len(nums)):
                try_traget = nums[i] + nums[j]
                if try_traget == target and i != j :
                    # Save the items in one array
                    return [i,j]



# Test------------------------------------------------------

objeto = Solution()
for i in range(3):
    case = {0: [2, 7, 11, 15], 1: [3,2 , 4], 2: [3,3]}
    targets = {0: 9,  1: 6, 2:6 }
    solutions = {0: [0, 1], 1: [1, 2], 2: [0, 1]}
    if objeto.twoSum(case[i], targets[i]) == solutions[i]:
        print(f"Test{i}: Accepted ")
    else:
         print("Tste + {i}: Failed")
    print(f"Output: {objeto.twoSum(case[i], targets[i])} \nExpected {solutions[i]} \n")
