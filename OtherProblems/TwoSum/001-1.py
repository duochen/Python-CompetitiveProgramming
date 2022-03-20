#Time Complexity: O(n)
#Space Complexity: O(n)
class Solution(object):
    def twoSum(self, nums, target):
        hash_map = {}
        for i in range(len(nums)):
            val = target - nums[i]
            if (val in hash_map.keys()):
                return (hash_map[val], i)
            else:
                hash_map[nums[i]] = i

s = Solution()
print(s.twoSum([3, 6, 12, 14], 15)) # (0, 2)
print(s.twoSum([2,7, 11, 15], 9)) # (0, 1)
print(s.twoSum([3,2,4], 6))  # (1, 2)
print(s.twoSum([3,3], 6))  # (0, 1)