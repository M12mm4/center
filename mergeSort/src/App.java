import java.util.Random;

public class App {
    public static void main(String[] args) {
        Random rand = new Random();

        int arr[] = new int[100];

        for (int index = 0; index < arr.length; index++) {
            arr[index] = rand.nextInt(1000);

            
        }

        mergeSort(arr);

        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i]);
            
        }



    }

    public static void mergeSort(int[] inputArray) {
        int len = inputArray.length;
        if(len < 2){
            return;
        }

        int mid = inputArray.length / 2;

        int[] leftHalf = new int[mid];
        int[] rightHalf = new int[inputArray.length - mid];

        for(int i = 0; i < mid; i++){
            leftHalf[i] = inputArray[i];
        }

        for(int i = mid; i < inputArray.length; i++){
            rightHalf[i-mid] = inputArray[i];
        }

        mergeSort(leftHalf);
        mergeSort(rightHalf);

        merge(inputArray, leftHalf, rightHalf);
    }

    public static void merge(int[] inputArray, int[] leftHalf, int[] rightHalf){
        int i = 0;
        int j = 0;
        int k = 0;

        while(i < leftHalf.length && j < rightHalf.length){
            if(leftHalf[i] <= rightHalf[j]){
                inputArray[k] = leftHalf[i];
                i++;
            }
            else{
                inputArray[k] = rightHalf[j];
                j++;
            }
            k++;
        }

        while(i < leftHalf.length){
            inputArray[k] = leftHalf[i];
            i++;
            k++;
        }
        while(j<rightHalf.length){
            inputArray[k] = rightHalf[j];
            j++;
            k++;
        }

    }
}
