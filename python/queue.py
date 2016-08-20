class Node:

    def __init__(self, data=None):
        self.data = data
        self.nextNode = None

class Queue:

    def __init__(self):
        self.head = None
        self.front_val = None
        self.back_val = None

    def empty(self):
        return not self.head

    def enqueue(self, data):
        newNode = Node(data=data)
        if self.empty():
            self.head = newNode
            self.front_val = self.back_val = data
        else:
            newNode.nextNode = self.head
            self.head = newNode
            self.back_val = data

    def dequeue(self):
        if not self.empty():
            if self.head.nextNode:
                b_cursor = self.head
                f_cursor = self.head.nextNode
                while f_cursor.nextNode:
                    b_cursor = f_cursor
                    f_cursor = f_cursor.nextNode

                return_data = f_cursor.data
                b_cursor.nextNode = None
                f_cursor = None
                self.front_val = b_cursor.data
                return return_data
            
            else:
                return_data = self.head.data
                self.head = None
                self.front_val = self.back_val = None
                return return_data

    def back(self):
        return self.back_val

    def front(self):
       return self.front_val
