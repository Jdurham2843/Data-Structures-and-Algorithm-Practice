""" Implementation for heap """

class Heap(object):
    
    def __init__(self, arr=[]):
        self.arr = arr
    
    def heapify(self, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and self.arr[left] > self.arr[largest]:
            largest = left
        
        if right < n and self.arr[right] > self.arr[largest]:
            largest = right
        
        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self.heapify(n, largest)
    
    def heap_sort(self):
        n = len(self.arr)

        for i in range(n, -1, -1):
            self.heapify(n, i)
        
        for i in range(n - 1, 0, -1):
            self.arr[i], self.arr[0] = self.arr[0], self.arr[i]
            self.heapify(i, 0)

    def insert(self, item):
        self.arr.append(item)
        self.heapify(len(self.arr), 0)
    
    def delete(self, item):
        index = self.search(item)
        if index:
            del self.arr[index]
            self.heapify(len(self.arr), 0)
            
    
    def search(self, item):
        result = self.find_item(item, 0)
        return result
    
    def find_item(self, item, i):
        if i > len(self.arr) - 1:
            return False
        else:
            if self.arr[i] == item:
                return i
            else:
                left = self.find_item(item, 2 * i + 1)
                right = self.find_item(item, 2 * i + 2)

                if left:
                    return left
                elif right:
                    return right
                else:
                    return False

def main():
    import random

    h1 = Heap()
    for i in range(0, 20):
        temp = random.randint(0, 100)
        h1.insert(temp)

    
    print(h1.arr)
    for i in range(len(h1.arr), -1, -1):
        h1.heapify(len(h1.arr), i)
    print(h1.arr)
    print("After sort:")
    h1.heap_sort()
    print(h1.arr)
    print("find {temp}".format(temp=temp))
    print(h1.search(temp))
    print("removing {temp}".format(temp=temp))
    h1.delete(temp)
    print(h1.arr)

if __name__ == '__main__':
    main()