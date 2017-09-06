import random

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    else:
        arr1 = merge_sort(arr[0:len(arr) // 2])
        arr2 = merge_sort(arr[len(arr) // 2: len(arr)])

        il = i2 = i = 0
        while il < len(arr1) or i2 < len(arr2):
            if il >= len(arr1):
                arr[i] = arr2[i2]
                i += 1
                i2 += 1
            elif i2 >= len(arr2):
                arr[i] = arr1[il]
                i += 1
                il += 1
            else:
                if arr1[il] < arr2[i2]:
                    arr[i] = arr1[il]
                    il += 1
                    i += 1
                else:
                    arr[i] = arr2[i2]
                    i2 += 1
                    i += 1
        return arr

if __name__ == '__main__':
    test_arrs = [[random.randint(0, 1000) for i in range(1, 21)] for num in range(1, 21)] 

    for i, test_arr in enumerate(test_arrs):
        print("Orignal {}: ".format(i), test_arr)
        print("Sorted {}: ".format(i), merge_sort(test_arr))