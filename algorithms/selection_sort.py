import random

def selection_sort(arr):
    end_index = len(arr) - 1
    while end_index != 0:
        forward_index = 0
        largest_num_index = end_index
        while forward_index < end_index:
            if arr[forward_index] > arr[largest_num_index]:
                largest_num_index = forward_index
            forward_index += 1
        
        if end_index != largest_num_index:
            temp = arr[end_index]
            arr[end_index] = arr[largest_num_index]
            arr[largest_num_index] = temp
        end_index -= 1
    return arr

if __name__ == '__main__':
    test_arrs = [[random.randint(0, 1000) for i in range(1, 21)] for num in range(1, 21)] 

    for i, test_arr in enumerate(test_arrs):
        print("Orignal {}: ".format(i), test_arr)
        print("Sorted {}: ".format(i), selection_sort(test_arr))