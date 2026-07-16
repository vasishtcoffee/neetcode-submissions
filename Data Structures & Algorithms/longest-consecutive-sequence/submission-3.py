class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set=set(nums)
        streak = 0
       
        for num in nums:
            if (num-1) not in num_set: 
                current_num = num
                count = 1

                while(current_num+1) in num_set:
                    count+=1
                    current_num +=1
                
        
                streak = max(count,streak)

        return streak
                   
        
