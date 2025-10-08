"""
1) Declare an Array named main_list to store all rows of the triangle.
2) Declare an Array named sub_list to store each row (current row elements).
3) Add 1 to the first sub_list (since the first row always starts with 1).
4) Add this sub_list to the main_list list (this forms the first row).
5) Iterate from the 0th row to numRows:
    i) Create a new sub_list and add 1 at the start (first element of each row is 1).
    ii) Get the previous row using prev_list = main_list.get(i).
    iii) Iterate through the previous row using a loop j = 0 to prev_list.size() - 1.
    iv) For each position, add the sum of prev_list.get(j) and prev_list.get(j + 1) to the new sub_list.
    v) After the loop, add 1 to the end of sub_list (last element is always 1).
    vi) Add this completed sub_list to the main_list list.
6) Return the main_list list containing all rows of Pascal’s Triangle.
"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        main_list = [] 
        sub_list = []
        sub_list.append(1)
        main_list.append(sub_list)
        for i in range(numRows ) : 
            sub_list = []
            sub_list.append(1)
            prev_list = main_list[i]
            for j in range (len(prev_list) - 1): 
                sub_list.append(prev_list[j] + prev_list[j+1])
            
            sub_list.append(1)
            main_list.append(sub_list)

        return main_list
