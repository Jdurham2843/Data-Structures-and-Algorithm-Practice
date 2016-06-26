class Node:

    def __init__(self, data, nextNode = None):
        self.data = data
        self.nextNode = nextNode

class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, value, position = None):
        newNode = Node(value)
        if self.head:
            cursor = self.head
            if position and position > 0:
                outOfRange = False
                while position > 1:
                    cursor = cursor.nextNode
                    if cursor == None and position > 1:
                        outOfRange = True
                        break
                    position -= 1
                if not outOfRange:
                    if cursor.nextNode == None:
                        cursor.nextNode = Node(value)
                    else:
                        newNode.nextNode = cursor.nextNode
                        cursor.nextNode = newNode

            elif position == None:
                while cursor.nextNode != None:
                    cursor = cursor.nextNode
                cursor.nextNode = newNode

            elif position == 0:
                newNode.nextNode = self.head
                self.head = newNode
        else:
            if not position:
                self.head = newNode


    def remove(self, value):
        if self.head:
            if self.head.data == value:
                self.head = self.head.nextNode
                return

            elif self.head.nextNode:
                bcursor = self.head
                fcursor = self.head.nextNode

                while fcursor != None:
                    if fcursor.data == value:
                        bcursor.nextNode = fcursor.nextNode
                        return
                    bcursor = fcursor
                    fcursor = fcursor.nextNode

    def reverse(self):
        if self.head and self.head.nextNode:
            previous = self.head
            present = self.head.nextNode
            previous.nextNode = None

            if present.nextNode:
                forward = present.nextNode
                while forward != None:
                    present.nextNode = previous
                    previous = present
                    present = forward
                    forward = forward.nextNode

            present.nextNode = previous
            self.head = present

    def find(self, value):
        if not self.head:
            return -1
        else:
            index = 0
            cursor = self.head
            while cursor != None:
                if cursor.data == value:
                    return index
                else:
                    cursor = cursor.nextNode
            return -1

    def __str__(self):
        if not self.head:
            return 'The list is empty'
        else:
            cursor = self.head
            printString = '[' + str(cursor.data)
            while cursor.nextNode != None:
                cursor = cursor.nextNode
                printString = printString + ', ' + str(cursor.data)
            printString = printString + ']'

            return printString
