#include <iostream>
#include <cstdlib>
#include <ctime>
#include <fstream>

#include "heap.h"

int main() {
    srand(time(NULL));
    Heap heap = Heap();

    std::ifstream testFile("test.txt");
    int size;
    testFile >> size;

    int itemToInsert;
    while ( testFile >> itemToInsert) {
        std::cout << "Inserting: " << itemToInsert << '\n';
        heap.insert(itemToInsert);
        std::cout << "Heap after insert: " << heap;
    }
    
    std::cout << "Presorted heap: ";
    std::cout << heap;

    heap.heapSort();

    std::cout << "After sort: " << heap;

    std::cout << "Searching for " << itemToInsert 
              << ". Found at " << heap.search(itemToInsert) << '\n';
    std::cout << "Removing " << itemToInsert << ".\n";

    std::cout << "Before removal: " << heap;

    heap.deleteItem(itemToInsert);
    std::cout << "After removal: " << heap;

    heap.heapSort();
    std::cout << "Resorted heap: " << heap;
}