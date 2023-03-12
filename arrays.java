import java.util.Arrays;

public class arrays {
    public static void main(String[] args) {
      String str = "fez day";
      int n = 0;
      String word = "";
      String[] words;
      for(int i = 0; i < str.length();i++){
          char chr = str.charAt(i); 
          if(Character.isLetter(chr)){
            word = word + chr;
          }else{
              words = new String[n+1];
              words[n] = word;
              n+=1;
              word = "";
              }
          }
      System.out.println(Arrays.toString( words ));

    }
}