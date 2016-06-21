class Node:
    val = None
    nextNode = None

class LinkedList:

    def __init__(self):
        self.root = None

    def empty(self):
        return False if self.root else True

    def insert(self, value, position = -1):
        if self.empty() and position > 0:
            print("The list have no position %d" % position)

        elif self.empty():
            newNode = Node()
            newNode.val = value
            self.root = newNode

        else:
            if position == 0:
                cursor = self.root
                newNode = Node()
                newNode.val = value
                newNode.nextNode = cursor.next
                self.root = newNode

            elif position == -1:
                cursor = self.root
                while cursor.nextNode != None:
                    cursor = cursor.next

                newNode = Node()



        '''else:
            cursor = self.root
            for index in range(0, position):
                if cursor == None:'''

    def find(self, value):
        if self.empty():
            return -1
        else:
            index = 0
            cursor = self.root
            while cursor != None:
                if cursor.val == value:
                    return index
                else:
                    cursor = cursor.nextNode
            return -1

    def __str__(self):
        if self.empty():
            return 'The list is empty'
        else:
            cursor = self.root
            printString = '[' + str(cursor.val)
            while cursor.nextNode != None:
                cursor = cursor.next
                printString = printString + ', ' + str(cursor.val)
            printString = printString + ']'

            return printString
