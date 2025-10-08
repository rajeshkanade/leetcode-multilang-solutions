// Approach : 
// 1) created two boolean array rows and column it stores true if on ith row position there occurs 0 then other wise by default false in Java
// 2) now iterate throw the matrix again then check if rows[i] or cols[j] is true if yes then make current index value 0

package Java.Arrays;

class SetMatrixZero {
    public void setZeroes(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;

        boolean rows[] = new boolean[m];
        boolean cols[] = new boolean[n];

        for(int i = 0 ; i < m ; i++){
            for(int j = 0 ; j < n ; j++){
                if(matrix[i][j] == 0){
                    rows[i] = true;
                    cols[j] = true;
                }
            }
        }


        for(int i = 0 ; i < m ; i++){
            for(int j = 0 ; j < n ; j++){
                if(rows[i] || cols[j]){
                    matrix[i][j] = 0;
                }
            }
        }
    }
   
}