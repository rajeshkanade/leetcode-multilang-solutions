function generate(numRows: number): number[][] {
    let list : number[][] = [];

    let subList : number[] = [];
    subList.push(1);
    list.push(subList);
    for(let i = 1 ; i < numRows ; i++){
        let prevList : number[] = list[i - 1];
        let subList : number [] = [];
        subList.push(1);
        for(let j = 0 ; j < prevList.length - 1 ; j++){
            subList.push(prevList[j] + prevList[j + 1]);
        }
        subList.push(1);
        list.push(subList);
    }

    return list;


};