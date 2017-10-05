#ifndef HEAP_H
#define HEAP_H

#include <vector>
#include <algorithm>
#include <string>

class Heap {
private:
    std::vector<int> arr;

    void heapify(int size, int index);

    int searchHelper(int index, int item);

    void completeHeapify();

public:
    Heap() {}

    void insert(int item);

    int search(int item);

    void deleteItem(int item);

    void heapSort();

    friend std::ostream& operator<<(std::ostream &strm, const Heap &heap);
};

#endif