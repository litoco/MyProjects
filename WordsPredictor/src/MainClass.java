import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class MainClass {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        MainClass mainClass = new MainClass();
        WordRelatedDetails rootWordEmptyString = new WordRelatedDetails();
        System.out.print("Enter a string now: ");
        String nextString = scan.nextLine();
        while (!nextString.equals("")){
            mainClass.train(rootWordEmptyString, nextString);
            System.out.println("Predicting result based on previous queries: ");
            mainClass.predict(rootWordEmptyString,"");
            System.out.print("Enter a string now (to close hit enter again): ");
            nextString = scan.nextLine();
        }
        System.out.println("Done execution");
    }

    private void predict(WordRelatedDetails wordRelatedDetails, String enteredString) {
        ArrayList<WordRelatedDetails> currWordRelatedDetails = wordRelatedDetails.getWordRelatedDetailsArrayList();
        if (currWordRelatedDetails==null || currWordRelatedDetails.size()==0) {
            System.out.println(enteredString+wordRelatedDetails.getWord());
        }else{
            Collections.sort(currWordRelatedDetails);
            for(int i=0;i<currWordRelatedDetails.size();i++) {
                predict(currWordRelatedDetails.get(i), enteredString + wordRelatedDetails.getWord());
            }
        }
    }

    private void train(WordRelatedDetails rootWordEmptyString, String enteredString) {
        rootWordEmptyString.train(enteredString, "", rootWordEmptyString);
    }
}
