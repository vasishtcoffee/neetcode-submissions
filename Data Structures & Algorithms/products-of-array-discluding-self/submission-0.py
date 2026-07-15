class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        carry_left = []
        multi = 1
        for index,num in enumerate(nums): 
            if (index==0):
                carry_left.append(1)
            else:
                
                multi = multi*nums[index-1]
                carry_left.append(multi)

        n= len(nums)
        suffix = [1] * n  
        for i in range(n-2,-1,-1):
            suffix[i]=suffix[i+1]*nums[i+1]
            
        output = [a * b for a, b in zip(carry_left,suffix)]
        return output 
        



            