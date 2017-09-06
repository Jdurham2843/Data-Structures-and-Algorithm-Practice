import random

def insertion_sort(arr):
    i = 1
    while i < len(arr):
        j = i - 1
        key = arr[i]
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        i += 1
    return arr

if __name__ == '__main__':
    test_arrs = [[random.randint(0, 1000) for i in range(1, 21)] for num in range(1, 21)] 

    for i, test_arr in enumerate(test_arrs):
        print("Orignal {}: ".format(i), test_arr)
        print("Sorted {}: ".format(i), insertion_sort(test_arr))