class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=collections.defaultdict(set)
        columns=collections.defaultdict(set)
        square=collections.defaultdict(set)

        for i in range(9):
            for j in range(9):
                val=board[i][j]
                if (val=='.'):
                    continue
                if(val in rows[i] or val  in columns[j]
                or val  in square[(i // 3 ,j // 3)]
                    ):
                    return False
                rows[i].add(val)
                columns[j].add(val)
                square[(i // 3 ,j // 3)].add(val)
            
        return True


        