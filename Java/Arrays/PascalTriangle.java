// java 
/*
1) Declare an ArrayList of lists named result to store all rows of the triangle.
2) Declare an ArrayList named subList to store each row (current row elements).
3) Add 1 to the first subList (since the first row always starts with 1).
4) Add this subList to the result list (this forms the first row).
5) Iterate from the 1nd row to numRows:
    i) Create a new subList and add 1 at the start (first element of each row is 1).
    ii) Get the previous row using prevList = result.get(i - 1).
    iii) Iterate through the previous row using a loop j = 0 to prevList.size() - 2.
    iv) For each position, add the sum of prevList.get(j) and prevList.get(j + 1) to the new subList.
    v) After the loop, add 1 to the end of subList (last element is always 1).
    vi) Add this completed subList to the result list.
6) Return the result list containing all rows of Pascal’s Triangle.
 */
package Java.Arrays;
import java.util.*;
class Solution {
    public List<List<Integer>> generate(int numRows) {
        ArrayList<List<Integer>> result = new ArrayList<>();
        if(numRows == 0 ) return result;
        ArrayList<Integer> list = new ArrayList<>();
        list.add(1);
        result.add(list);
        if(numRows == 1) return result;

        for(int i = 1 ; i < numRows ; i++){
            List<Integer> l = result.get(i - 1);
            ArrayList<Integer> newList = new ArrayList<>();
            newList.add(1);
            for(int j = 0 ; j < i - 1 ; j++){
                newList.add(l.get(j) + l.get(j + 1));
            }
            newList.add(1);
            result.add(newList);
        }
        return result;
    }
}
    