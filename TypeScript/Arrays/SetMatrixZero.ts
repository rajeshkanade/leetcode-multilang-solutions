/**
 Do not return anything, modify matrix in-place instead.
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

