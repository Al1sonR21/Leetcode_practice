class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        # Create the array ans
        ans = []
        # Append in the position i nums[nums[i]]       
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        return ans