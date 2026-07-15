class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for col in range(9):
            seen = set()

            for row in range(9):
                val = board[row][col]
                if val==".":
                    continue 
                elif val in seen:
                    return False
                else:
                    seen.add(val)

        for row in board: 
            seen=set()
            for num in row: 
                if num==".":
                    continue
                elif num in seen:
                    return False
                else:
                    seen.add(num)
    
        for r_start in range(0, 9, 3):
            for c_start in range(0, 9, 3):
        
                seen = set()
        
        
        
                for r in range(r_start, r_start + 3):
                    for c in range(c_start, c_start + 3):
                        val = board[r][c]
                
               
                        if val == ".": 
                            continue
                    
                        if val in seen:
                            return False
                        else:
                             seen.add(val)
        return True
