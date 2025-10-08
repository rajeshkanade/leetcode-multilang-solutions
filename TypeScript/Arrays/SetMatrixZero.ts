/**
 Do not return anything, modify matrix in-place instead.
   Approach : 
  1) created two boolean array rows and column it stores true if on ith row position there occurs 0 then other wise by default no false we have to set to false
  eg. 
  let rows : boolean[] = new Array(matrix.length).fill(false);  // create the false value according to length of array 
  same for columns 
  2) now iterate throw the matrix again then check if rows[i] or cols[j] is true if yes then make current index value 0
 */

function setZeroes(matrix: number[][]): void {
let rows : boolean[] = new Array(matrix.length).fill(false);
let cols : boolean[] = new Array(matrix[0].length).fill(false);
    for(let i : number = 0 ; i < matrix.length ; i++){
        for(let j : number = 0 ; j < matrix[i].length ; j++){
            if(matrix[i][j] == 0){
                rows[i] = true;
                cols[j] = true;
            }
        }
    }


    for(let i : number = 0 ; i < matrix.length ; i++){
        for(let j : number = 0 ; j < matrix[i].length ; j++){
            if(rows[i] == true || cols[j] == true){
                matrix[i][j] = 0;
            }
        }

    }
};

