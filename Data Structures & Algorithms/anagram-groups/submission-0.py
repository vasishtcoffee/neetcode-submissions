class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        if len(strs) == 0 : 
            return []
        for str in strs: 
            letter=sorted(str)
            key="".join(letter)
            if key not in d: 
                d[key] = []
                d[key].append(str)
            else: 
                d[key].append(str)
                
        return list(d.values())