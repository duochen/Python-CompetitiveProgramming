#Time Complexity: O(n)
#Space Complexity: O(n)
class Solution:
    def twoSum(self, nums, target):
        m = {}
        n = len(nums)
        for i in range(0,n):
            goal = target - nums[i]
            if(goal in m):
                return [m[goal], i]
            m[nums[i]] = i

s = Solution()
print(s.twoSum([3, 6, 12, 14], 15))
        