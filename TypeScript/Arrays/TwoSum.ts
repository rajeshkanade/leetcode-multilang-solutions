//  Two Sum Approach 
//  1) created the hashmap to store the each number as key and it index as value   such that if complement == number present in hashmap then for getting the value as an index
//  eg. here is no inbuilt hashmap in python so dictionary is used as hash map
        // let hashMap : Record<number,number> = {}
        // Record is a generic type in typescript used to define a type for an object
//  2) Iterate using for loop and calculate the complement 
//  3) If complement present in hashKey then return current index of element and value of that complement from the hashmap
//  4) Otherwise current number in hashMap as key and it index as value 
//  5) If no two number are present then return the empty array 
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