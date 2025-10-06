function twoSum(nums: number[], target: number): number[] {
    let hashMap : Record<number,number> = {} 
    
    for(let i : number = 0 ; i < nums.length ; i++){
        let complement : number = target - nums[i];
        if(complement in hashMap) {
            return [hashMap[complement] , i]
        }
        hashMap[nums[i]] =  i;
    }
    return [];
};