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