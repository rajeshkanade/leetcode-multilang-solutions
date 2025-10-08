/* 
 * Two Sum Approach 
 * 1) created the hashmap to store the each number as key and it index as value   such that if complement == number present in hashmap then for getting the value as an index
 * eg. HashMap<Integer,Integer> map = new HashMap<>();
 * 2) Iterate using for loop and calculate the complement 
 * 3) If complement present in hashKey then return current index of element and value of that complement from the hashmap
 * 4) Otherwise current number in hashMap as key and it index as value 
 * 5) If no two number are present then return the empty array 
 * 
 */

package Java.Arrays;
import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> map = new HashMap<>();

        for(int i = 0 ; i < nums.length ; i++){
            int complement = target - nums[i];
            if(map.containsKey(complement)){
                return new int [] {map.get(complement) , i};
            }
            map.put(nums[i] , i);
        }
        return new int[] {};
    }
}