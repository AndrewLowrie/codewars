package EightKyu;

// Write function avg which calculates average of numbers in given list.

public class CalculateAverage {

    public static double find_average(int[] array){

        int sum = 0;
        for (int i = 0; i < array.length; i++) {
            sum += array[i];
        }
        
        return sum / array.length * 1.0;

    }

    public static void main(String[] args) {

        CalculateAverage.find_average(new int[]{1,1,1});   // 1
        CalculateAverage.find_average(new int[]{1, 2, 3}); // 2

    }

}