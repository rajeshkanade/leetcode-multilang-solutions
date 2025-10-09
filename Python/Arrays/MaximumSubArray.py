"""
            
here kadane's algorithm is used 
Apporach : 
i) Declare two variables: sum for current sum and maxSum for maximum sum.
ii) Initialize maxSum with the lowest negative value (or -inf) and sum to 0.
iii) Loop through each element in the array.
iv) Add the current element to sum.
v) If sum > maxSum, update maxSum with sum.
vi) If sum < 0, reset sum to 0.
Reason: Adding any number to a negative sum will reduce it, so we reset sum to 0 to start a new potential subarray (we want the maximum subarray sum).
vii) After the loop ends, return maxSum.
                 
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float(-inf)
        sum = 0
        for i in range(len(nums)) : 
            sum += nums[i]
            maxSum = max(maxSum , sum)
            if(sum < 0) : 
                sum = 0 
        return maxSum
