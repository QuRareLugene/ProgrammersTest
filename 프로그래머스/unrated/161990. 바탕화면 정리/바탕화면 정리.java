class Solution {
    public int[] solution(String[] wallpaper) {
        int UpYCoordinate = 60, UpXCoordinate = 60, DownYCoordinate = -1, DownXCoordinate = -1;
        for(int i=0;i<wallpaper.length;i++){
            for(int j=0;j<wallpaper[i].length();j++){
                if (wallpaper[i].charAt(j) == '#'){
                    if (i < UpYCoordinate){
                        UpYCoordinate = i;
                    }
                    if (j < UpXCoordinate){
                        UpXCoordinate = j;
                    }
                    if (i > DownYCoordinate){
                        DownYCoordinate = i;
                    }
                    if (j > DownXCoordinate){
                        DownXCoordinate = j;
                    }
                }
            }
        }
        int[] answer = {UpYCoordinate, UpXCoordinate, DownYCoordinate+1, DownXCoordinate+1};
        return answer;
    }
}