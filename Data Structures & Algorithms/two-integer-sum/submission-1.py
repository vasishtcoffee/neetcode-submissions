class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            new_num = target - nums[i]
            if new_num in d:
                if (i<d.get(new_num) and i!=d.get(new_num)):
                    return [ i , d.get(new_num)]
                elif (i>d.get(new_num) and i!=d.get(new_num)) : 
                    return [d.get(new_num),i]
                else: 
                    exit 
            else : 
                d[nums[i]]=i
            

                
            