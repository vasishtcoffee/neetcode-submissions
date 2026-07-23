class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map={}
        window_start=0
        window_size=0
        longest=0
        for i in range(len(s)):
            if s[i] in hash_map:
                if hash_map[s[i]]+1>window_start: #consider the case abba
                    window_start=hash_map[s[i]]+1 
            hash_map[s[i]]=i
            window_size = i-window_start+1
            if window_size>longest:
                longest=window_size
        return longest