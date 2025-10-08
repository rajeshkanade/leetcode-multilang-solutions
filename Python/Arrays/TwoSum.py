#  Two Sum Approach 
#  1) created the hashmap to store the each number as key and it index as value   such that if complement == number present in hashmap then for getting the value as an index
#  eg. here is no inbuilt hashmap in python so dictionary is used as hash map
        # hash_map = {}
#  2) Iterate using for loop and calculate the complement 
#  3) If complement present in hashKey then return current index of element and value of that complement from the hashmap
#  4) Otherwise current number in hashMap as key and it index as value 
#  5) If no two number are present then return the empty array 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i , num in enumerate(nums):
            complement = target - num
            if complement in hash_map : 
                return [hash_map[complement] , i]
            
            hash_map[num] = i
        
        # return []

        # for i, num1 in enumerate(nums ) : 
        #     for j , num2 in enumerate(nums) : 
        #         if(num1 + num2 == target) : 
        #             return [i , j]
        
        # for i in range(len(nums)) : 
        #     for j in range(i + 1 , len(nums)) : 
        #         if (nums[i] + nums[j] == target) :
        #             return [i , j]

        return []

    
    """ 
     target = 9 
     9 - 2 = 7 
     hash_map = {} -- false 
     hash_map[2] = 0

     9 -> target 
     9 - 7 => 2 

     [0 , 1]

    """