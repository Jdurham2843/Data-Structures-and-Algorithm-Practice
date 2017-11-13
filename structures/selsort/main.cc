#include <iostream>
#include <vector>
#include <ctime>
#include <cstdlib>

void selectionSort(std::vector<int> &arr) {
    for(int n = arr.size(); n > 0; n--) {
        int largest = n;
        for(int i = 0; i < n; i++) {
            if (arr[i] > arr[n]) {
                largest = i;
            }
        }

        if (largest != n) {
            int temp = arr[n];
            arr[n] = arr[largest];
            arr[largest] = temp;
        }
    }
}

int main() {
    std::vector<int> arr;
    srand(time(NULL));
    for (int i = 0; i < 20; i++) {
        arr.push_back(rand() % 100 + 1);
    }

    selectionSort(arr);
    for (int i = 0; i < 20; i++) {
        std:: cout << arr[i] << ", ";
    }
    std::cout << '\n';

    
    for (int i = 0; i < 20; i++) {
        std:: cout << arr[i] << ", ";
    }
    std::cout << '\n';



    return 0;
}