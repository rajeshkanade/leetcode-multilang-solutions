class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows_bool = [False] * len(matrix)
        cols_bool = [False] * len(matrix[0])

        
        for row in range(len(matrix)):
            for col in range(len(matrix[row])) :
                if(matrix[row][col] == 0) :
                    rows_bool[row] = True
                    cols_bool[col] = True
               

        for row in range(len(matrix)):
            for col in range(len(matrix[row])) :
                if(rows_bool[row] or cols_bool[col]):
                    matrix[row][col] = 0
                
        
        