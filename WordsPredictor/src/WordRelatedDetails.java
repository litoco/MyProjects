import java.util.ArrayList;

public class WordRelatedDetails implements Comparable{

    private String word="";
    private int wordOccurrence;
    private ArrayList<WordRelatedDetails> wordRelatedDetailsArrayList;

    public void setWord(String word) {
        this.word = word;
    }

    public String getWord() {
        return word;
    }

    public void setWordOccurrence(int wordOccurrence) {
        this.wordOccurrence = wordOccurrence;
    }

    public int getWordOccurrence() {
        return wordOccurrence;
    }

    public ArrayList<WordRelatedDetails> getWordRelatedDetailsArrayList() {
        return wordRelatedDetailsArrayList;
    }

    public void setWordRelatedDetailsArrayList(ArrayList<WordRelatedDetails> wordRelatedDetailsArrayList) {
        this.wordRelatedDetailsArrayList = wordRelatedDetailsArrayList;
    }

    public void train(String enteredString, String prevString, WordRelatedDetails currentWordRelatedDetailsObject) {
        if(enteredString.equals(""))
            return;

        if (!prevString.equals(" ") || !String.valueOf(enteredString.charAt(0)).equals(prevString)) {

            if (currentWordRelatedDetailsObject.getWordRelatedDetailsArrayList() == null)
                currentWordRelatedDetailsObject.setWordRelatedDetailsArrayList(new ArrayList<>());

            //loop to find out whether the string at index 0 of enteredString is present in the list or not
            WordRelatedDetails wordRelatedDetails = null;
            for (WordRelatedDetails currentWordRelatedDetails : currentWordRelatedDetailsObject.getWordRelatedDetailsArrayList()) {
                if (currentWordRelatedDetails.getWord().equals(String.valueOf(enteredString.charAt(0)))) {
                    wordRelatedDetails = currentWordRelatedDetails;
                    break;
                }
            }

            /*if there is no word in the list that match the string at index 0 of enteredString
              then, create new wordObject and assign the word string to that object
              else if, the word is found then increase is occurrence by 1 */
            if (wordRelatedDetails == null) {
                wordRelatedDetails = new WordRelatedDetails();
                wordRelatedDetails.setWord(String.valueOf(enteredString.charAt(0)));
                wordRelatedDetails.setWordOccurrence(0);
                currentWordRelatedDetailsObject.getWordRelatedDetailsArrayList().add(wordRelatedDetails);
            } else
                wordRelatedDetails.setWordOccurrence(wordRelatedDetails.getWordOccurrence()+1);

            // recursively call train() method with substring of enteredString to train this data set
            wordRelatedDetails.train(enteredString.substring(1), String.valueOf(enteredString.charAt(0)), wordRelatedDetails);

        }else{
            currentWordRelatedDetailsObject.train(enteredString.substring(1), " ", currentWordRelatedDetailsObject);
        }
    }

    @Override
    public int compareTo(Object o) {
        int compareOccurrences = ((WordRelatedDetails)o).wordOccurrence;
        return compareOccurrences-this.wordOccurrence;//for descending order
//        return this.wordOccurrence-compareOccurrences;//for ascending order
    }
}
