/*Implement the Heap/Shell sort algorithm implemented in Java
demonstrating heap/shell data structure with modularity of
programming language. */

import java.util.Arrays;

public class Assign11{
    
    // Implementation of Heap Sort
    
    public static void heapSort(int[] array) {
        int n = array.length;

        // Build max heap
        for (int i = n / 2 - 1; i >= 0; i--) {
            heapify(array, n, i);
        }

        // Extract elements from the heap one by one
        for (int i = n - 1; i > 0; i--) {
            // Move current root to the end
            int temp = array[0];
            array[0] = array[i];
            array[i] = temp;

            // Heapify the reduced heap
            heapify(array, i, 0);
        }
    }

    private static void heapify(int[] array, int n, int i) {
        int largest = i;
        int left = 2 * i + 1;
        int right = 2 * i + 2;

        // If left child is larger than root
        if (left < n && array[left] > array[largest]) {
            largest = left;
        }

        // If right child is larger than largest so far
        if (right < n && array[right] > array[largest]) {
            largest = right;
        }

        // If largest is not the root
        if (largest != i) {
            int swap = array[i];
            array[i] = array[largest];
            array[largest] = swap;

            // Recursively heapify the affected sub-tree
            heapify(array, n, largest);
        }
    }

    // Implementation of Shell Sort

    public static void shellSort(int[] array) {
        int n = array.length;

        // Start with a large gap and reduce it
        for (int gap = n / 2; gap > 0; gap /= 2) {
            // Perform insertion sort on elements separated by gap
            for (int i = gap; i < n; i++) {
                int temp = array[i];
                int j;
                for (j = i; j >= gap && array[j - gap] > temp; j -= gap) {
                    array[j] = array[j - gap];
                }
                array[j] = temp;
            }
        }
    }

    public static void main(String[] args) {
        int[] array1 = {9, 2, 5, 1, 7, 4, 8, 3, 6};
        int[] array2 = {9, 2, 5, 1, 7, 4, 8, 3, 6};

        System.out.println("Original Array: " + Arrays.toString(array1));

        heapSort(array1);
        System.out.println("Sorted using Heap Sort: " + Arrays.toString(array1));

        shellSort(array2);
        System.out.println("Sorted using Shell Sort: " + Arrays.toString(array2));
    }
}
