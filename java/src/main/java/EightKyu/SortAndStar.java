package EightKyu;

//You will be given an vector of string(s). You must sort it alphabetically (case-sensitive!!) and then return the first value.

//The returned value must be a string, and have "***" between each of its letters.

//You should not remove or add elements from/to the array.

public class SortAndStar {

    public static String twoSort(String[] s) {

        String earliestElement = s[0];

        for (int i = 1; i < s.length; i++) {
            if (s[i].charAt(0) < earliestElement.charAt(0)) {
                earliestElement = s[i];
            }
        }

        String result = "";
        for (int i = 0; i < earliestElement.length()-1; i++) {
            result += earliestElement.charAt(i) + "***";
        }
        result += earliestElement.charAt(earliestElement.length()-1);

        return result;

    }

    public static void main(String[] args) {

        SortAndStar.twoSort(new String[] {"bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"});
        SortAndStar.twoSort(new String[] {"turns", "out", "random", "test", "cases", "are", "easier", "than", "writing", "out", "basic", "ones"});

    }

}

