class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r//3) , (c//3)]):
                    return False

                char = board[r][c]
                cols[c].add(char)
                rows[r].add(char)
                squares[(r//3),(c//3)].add(char)

        return True
        
