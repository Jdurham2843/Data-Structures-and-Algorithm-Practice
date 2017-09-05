class Node:

    def __init__(self, data=None):
        self.data = data
        self.nextNode = None 

class Stack:

    def __init__(self):
        self.head = None

    def push(self, data):
        if not self.empty():
            cursor = self.head
            while cursor.nextNode:
                cursor = cursor.nextNode

            newNode = Node(data=data)
            cursor.nextNode = newNode

        else:
            newNode = Node(data=data)
            self.head = newNode

    def pop(self):
        if not self.empty():
            if not self.head.nextNode:
                return_data = self.head.data
                self.head = None
                return return_data

            else:
                b_cursor = self.head
                f_cursor = b_cursor.nextNode
                while f_cursor.nextNode:
                    b_cursor = f_cursor
                    f_cursor = f_cursor.nextNode

                b_cursor.nextNode = None
                return_data = f_cursor.data
                f_cursor = None
                return return_data

    def empty(self):
        return not self.head

    def top(self):
        if not self.empty():
            cursor = self.head
            while cursor.nextNode:
                cursor = cursor.nextNode

            return cursor.data



