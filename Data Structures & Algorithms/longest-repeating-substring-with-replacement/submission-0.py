class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_map={}
        window_start=0
        max_frequency=0
        window_length=0
        answer=0
        for i in range(len(s)):
            if s[i] in hash_map:
                hash_map[s[i]]+=1
            else:
                hash_map[s[i]]=1

            window_length = i- window_start + 1 
            max_frequency = max(hash_map.values())
            
            while window_length-max_frequency > k :
                hash_map[s[window_start]]-=1
                window_start+=1 
                window_length = i- window_start + 1     
                max_frequency = max(hash_map.values())

            answer=max(window_length,answer)

        return answer 






      
