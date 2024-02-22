class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        hold = nums[0]
        for i in range(1, n):
            if hold <= 0 and i != n: # can't move
                return False
            elif hold > 0: # can still move forward to the end index
                if nums[i] >= hold:
                    hold = nums[i] # replace with the next non-decreasing number
                    continue
                else:
                    hold -= 1
                    continue
            
        return True
        