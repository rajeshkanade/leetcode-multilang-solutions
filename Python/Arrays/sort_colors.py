# Used Merge Sort to solve this problem 
# Approach : 
    # 1) merge is an divide and conquour apporach 
    # 2) created the merge_sort function to divide the array into left and right
    # 3) when merge_sort function divide the array in single element then merge function is called to merge them
    # 4) merge function is used to merge the two sorted array
    # 5) In merge function two arrays are merge in sorted order 
    # 6) merge array into temparary array 
    # 7) copy the temp array into original array
    # 8) Time Complexity : O(nlogn)

class Solution:

    def merge(self , nums:List[int] , l : int , m:int , r:int) -> None : 
        i = l 
        j = m + 1
        temp = []
        while(i <= m and j <= r) :
            if(nums[i] <= nums[j]) :
                temp.append(nums[i])
                i += 1
            else :
                temp.append(nums[j])
                j += 1
        
        while(i <= m) :
            temp.append(nums[i])
            i+=1
        while(j <= r) :
            temp.append(nums[j])
            j += 1
        for k in range(len(temp)):
            nums[l + k] = temp[k]


    def merge_sort(self , nums:List[int], l:int , r:int) -> None:
        if(l < r) :
            m: int = l + (r - l) // 2
            self.merge_sort(nums, l , m)
            self.merge_sort(nums , m + 1 , r)
            self.merge(nums, l , m , r)
        
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.merge_sort(nums , 0 , len(nums) - 1)
        