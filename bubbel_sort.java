package Sorting;

public class bubble_soter {
static void sort(int arr[]){
    //asending order
    int n=arr.length;
    for(int i=0;i<n-1;i++){
        for(int j=0;j<n-i-1;j++){
            if(arr[j]>arr[j+1]){
            int temp=arr[j+1];
            arr[j+1]=arr[j];
            arr[j]=temp;
        }
    }
    }
}
    public static void main(String[] args) {
        int arr[]={210,270,190,180,230};
        sort(arr);
        for(int a:arr){
            System.out.println(a+" ");
        }
    
}
}