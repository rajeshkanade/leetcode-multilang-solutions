#  Approach : 
#  1) created two boolean array rows and column it stores true if on ith row position there occurs 0 then other wise by default no false we have to set to false 
# rows_bool = [False] * len(matrix)  and cols_bool = [False] * len(matrix[0]) create the false value according to length of array 
#  2) now iterate throw the matrix again then check if rows[i] or cols[j] is true if yes then make current index value 0

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
                
        
        