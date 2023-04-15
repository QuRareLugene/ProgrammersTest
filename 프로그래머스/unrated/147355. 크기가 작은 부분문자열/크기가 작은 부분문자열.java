class Solution {
    public int solution(String t, String p) {
        long GivenNum = Long.parseLong(p);
        int count = 0;
        long CompareNum = 0;
        
        for(int i=0;i<(t.length()-p.length()+1);i++){
            CompareNum = Long.parseLong(t.substring(i,i+p.length()));
            if (CompareNum <= GivenNum){
                count++;
            }
            // System.out.println("CompareNum = " + CompareNum);
            // System.out.println("GivenNum = " + GivenNum);
            // System.out.println("Count = " + count);
        }
        
        return count;
    }
}