#include <iostream>
#include <stdlib.h>
#include <time.h>
 
int ARRAY_SIZE = 10;
 
void insertion_sort(int *arr, int size) {
  for ( int i = 0; i < size; i++ ) {
    int key = arr[i];
    int j = i - 1;
    while (( j >= 0) && key < arr[j]) {
      arr[j+1] = arr[j];
      j--;
    }
    arr[j+1] = key;
  }
}

int* merge_sort(int *arr, int size) {
  if (size == 1) {
    return arr;
  } else {
    
    // setup for the merging
    int arr_size_0 = 0;
    int arr_size_1 = 0;
    
    if (size % 2 == 0) {
      arr_size_0 = arr_size_1 = size / 2;
    } else {
      arr_size_0 = (size / 2) + 1;
      arr_size_1 = (size / 2);
    }
    
    int arr0[arr_size_0];
    for ( int i = 0; i < arr_size_0; i++ ) {
      arr0[i] = arr[i];
    }
    
    int arr1[arr_size_1];
    for ( int i = 0; i < arr_size_1; i++ ){
      arr1[i] = arr[arr_size_1 + i];
    }
    
    int *arr0_sorted = merge_sort(arr0, arr_size_0);
    int *arr1_sorted = merge_sort(arr1, arr_size_1);
    
    int i0, i1, i = 0;
    while ((i0 < arr_size_0) || (i1 < arr_size_1)) {
      if (i0 >= arr_size_0) {
        arr[i] = arr1_sorted[i1];
        i++;
        i1++;
      } else if ( i1 >= arr_size_1 ) {
        arr[i] = arr0_sorted[i0];
        i++;
        i0++;
      } else {
        if (arr0_sorted[i0] < arr1_sorted[i1]) {
          arr[i] = arr0_sorted[i0];
          i0++;
          i++;
        } else {
          arr[i] = arr1_sorted[i1];
          i1++;
          i++;
        }
      }
    }
    
    for (int i = 0; i < ARRAY_SIZE; i++ ) {
      std::cout << arr_sorted[i] << ' ';
    }
    std:: cout << "\n\n";
    return arr;
    
  }
}
 
int main() {
  srand(time(NULL));
  int arr[ARRAY_SIZE];
  for (int num = 0; num < ARRAY_SIZE; num++ ) {
    arr[num] = rand() % ARRAY_SIZE;
  }
  
  std::cout << "Original sequence: \n";
  for (int i = 0; i < ARRAY_SIZE; i++ ) {
    std::cout << arr[i] << ' ';
  }
  std:: cout << "\n\n";
  
  int *arr_sorted = merge_sort(arr, ARRAY_SIZE);
  std::cout << "Sorted sequence: \n";
  for (int i = 0; i < ARRAY_SIZE; i++ ) {
    std::cout << arr_sorted[i] << ' ';
  }
  std:: cout << "\n\n";
  
}
