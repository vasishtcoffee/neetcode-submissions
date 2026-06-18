class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        if len(strs) == 0 : 
            return []
        for str in strs: 
            letter=sorted(str)
            key="".join(letter)
            
        
            d[key].append(str)
                
        return list(d.values())