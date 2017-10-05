""" Heap sort python implementation """

def heapify(arr, n, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        temp = arr[largest]
        arr[largest] = arr[i]
        arr[i] = temp

        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)
 
    # Build max heap
    for i in range(n, 0, -1):
        heapify(arr, n, i)
 
    
    for i in range(n-1, 0, -1):
        # swap
        arr[i], arr[0] = arr[0], arr[i]  
        
        #heapify root element
        heapify(arr, i, 0)


    
