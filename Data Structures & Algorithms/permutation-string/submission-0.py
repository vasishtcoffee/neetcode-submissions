class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size=0
        window_start=0
        window_length=0
        hash_map1={}
        hash_map2={}
        for i in range(len(s1)):
            if s1[i] in hash_map1:
                hash_map1[s1[i]]+=1
            else:
                hash_map1[s1[i]]=1

        for i in range(len(s2)):
           
            if s2[i] not in hash_map1:
                window_start=i+1
                hash_map2={}
                continue
            window_length = i-window_start+1
            
            if s2[i] in hash_map2:
                hash_map2[s2[i]]+=1
            else:
                hash_map2[s2[i]]=1
            if window_length>len(s1):
                left_char=s2[window_start]
                hash_map2[left_char]-=1
                
                if hash_map2[left_char]==0:
                    del hash_map2[left_char]
                window_start+=1
            window_length = i-window_start+1
            if window_length==len(s1):
                if hash_map1==hash_map2:
                    return True 
        
        return False
        