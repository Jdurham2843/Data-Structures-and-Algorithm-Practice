#include "heap.h"
#include <iostream>
#include <algorithm>

void Heap::heapify(int size, int index) {
    int left = 2 * index + 1;
    int right = 2 * index + 2;
    int largest = index;

    if ((left < size) && (arr[left] > arr[largest])) {
        largest = left;
    }

    if ((right < size) && (arr[right] > arr[largest])) {
        largest = right;
    }

    if (largest != index) {
        std::swap(arr[index], arr[largest]);
        heapify(size, largest);
    }
}

int Heap::searchHelper(int index, int item) {
    if (index > arr.size() - 1) {
        return -1;
    } else {
        if (arr[index] == arr[item]) {
            return index;
        } else {

            if (arr[index] == item) {
                return index;
            }

            int left = searchHelper(2 * index + 1, item);
            int right = searchHelper(2 * index + 2, item);

            if (left != -1) {
                return left;
            } else {
                return right;
            }
        }
    }
}

void Heap::completeHeapify() {
    int size = arr.size();

    for ( int i = size / 2 - 1; i >= 0; i-- ) {
        heapify(size, i);
    }
}

void Heap::insert(int item) {
    arr.push_back(item);
    completeHeapify();
}

int Heap::search(int item) {
    return searchHelper(0, item);
}

void Heap::deleteItem(int item) {
    int index = search(item);

    if (index != -1) {
        arr.erase(arr.begin() + index);
        completeHeapify();
    }
}

void Heap::heapSort() {
    int size = arr.size();

    completeHeapify();

    for ( int i = size - 1; i > 0; i-- ) {
        std::swap(arr[i], arr[0]);
        heapify(i, 0);
    }
}

std::ostream& operator<<(std::ostream &strm, const Heap &heap) {
    strm << '[';
    for( int i = 0; i < heap.arr.size(); i++ ) {
        strm << heap.arr[i] << ", " ;
    }
    return strm << "]\n";
}