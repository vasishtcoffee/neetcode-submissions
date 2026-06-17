class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1={}
        d2={}
        count1=0
        count2=0
        for char in s: 
            if char in d1:
                d1[char] = d1[char] + 1
            
            else:
                count1 = count1 + 1
                d1[char]= count1 
            count1 = 0 
        for char in t: 
            if char in d2:
                d2[char] = d2[char] + 1
                
            else:
                count2 = count2 + 1
                d2[char]= count2 
            count2 = 0 
        if (d1==d2):
            return True 
        else:
            return False 

            
