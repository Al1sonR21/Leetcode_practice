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


# Test parameters
param_1 = [3,3]
param_2 = 6

# Test
objeto = Solution()
print(objeto.twoSum(param_1, param_2))