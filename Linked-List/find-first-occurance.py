# RETURNS ZERO BASED INDEX OF THE FIRST OCCURRENCE OF A GIVEN DATA IN THE LINKED LIST
class Node :
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    def setNext(self, value):
        self.next = value

class LinkedList :
    def __init__(self, head = None):
        self.head = head
    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.setNext(Node(data))
    def find(self, data):
        if self.head is None:
            return "empty"
        elif (self.head.data == data):
           return 0
        else:
            INDEX = 0
            temp = self.head
            flag = False
            while temp:
                if temp.data == data:
                    return INDEX
                else:
                    temp = temp.next
                    INDEX += 1
            if flag == False:
                return (-1)
ll = LinkedList(Node('a'))
ll.append('b')
ll.append('c')
ll.append('d')
ll.append('e')
ll.append('f')
print(ll.find('e'))
print(ll.find('as'))