import java.util.*;

public class Solution {
    public Integer[] solution(int []arr) {
        ArrayList<Integer> answer = new ArrayList<Integer>();
        answer.add(arr[0]);
        for(int i=1;i<arr.length;i++){
            int recentnum = arr[i-1];
            if (arr[i] != recentnum){
                answer.add(arr[i]);
            }
        }
        
        Integer[] result = answer.toArray(new Integer[answer.size()]);
        return result;
    }
}