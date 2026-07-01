# ----For the leetcode problem "Two Sum"----

class Solution(object):
    def two_sum(self, nums, target):
        
        num_map = {}
        for i, num in enumerate(nums): complement = target - num
        if complement in num_map:
                return [num_map[complement], i]
        num_map[num] = i
        return []
    

# --- For your own value(example)-----
class Solution:
    def two_sum(self, nums, target):
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []
    
nums = [2, 7, 11, 15]
target = 9
solution = Solution()
result = solution.two_sum(nums, target)
print(result)  

