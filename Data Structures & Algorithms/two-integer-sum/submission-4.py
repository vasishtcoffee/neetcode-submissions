class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            new_num = target - nums[i]
            if new_num in d:
                return [d[new_num],i]            
            else : 
                d[nums[i]]=i
                

                
            