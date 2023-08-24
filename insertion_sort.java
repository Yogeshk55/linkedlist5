package Sorting;

public class insertion_sort {
    static void sort(int arr[]){
        int n = arr.length;
        for (int i=1;i<n;i++) {
            int temp= arr[i];
            int j= i-1;

            while (j>=0 && arr[j]>temp) {
                arr[j+1]=arr[j];
                j=j-1;
            }
            arr[j+1]=temp;
        }
    }
    public static void main(String[] args) {
        int arr[]={170,150,210,180,300};
        sort(arr);
        for(int x:arr){
            System.out.println(x+" ");
        }
    }
}
