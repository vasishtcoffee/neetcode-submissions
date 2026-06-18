class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        arr = []
        bucket = [[] for _ in range(len(nums) + 1)]
        for num in nums:            
            key = num 
            d[key] =  d.get(key,0) + 1

            # bucket[1] = 1 
            # bucket[2] = 2 

        for number,frequency in d.items():   
            bucket[frequency].append(number)

        for i in range(len(nums), 0, -1 ):
            for number in bucket[i]:
                arr.append(number)
                if len(arr)==k:
                    return arr
            #for every element increase the count in the corresponding index            
            # check the count against the value k 
            # if count >=k , return those elements in a list 

