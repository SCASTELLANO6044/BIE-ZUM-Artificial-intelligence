import java.io.*;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
       File infile = new File("C:/CTU/Summer Semester/BIE-ZUM Artificial Intelligence Fundamentals/Homeworks/bie-zum-homework01/8puzzle");
       try(BufferedReader buffer = new BufferedReader(new FileReader(infile))){
           String line;
           try{
               ArrayList<String> outHeuristic1 = new ArrayList<>();
               ArrayList<String> outHeuristic2 = new ArrayList<>();

               while ((line = buffer.readLine())!=null){
                   String[] tokens = line.split(",");
                   int[] state = new int[9];
                   int i = 0;
                   for( String current : tokens){
                       state[i] = Integer.parseInt(current);
                       i++;
                   }
                   Node nodeA = new Node(state);
               }
           }catch (Exception e){
               System.out.println("Algo ha ido mal");
           }
       }catch (Exception e){
           System.out.println("Algo ha ido mal");
       }
    }
}
