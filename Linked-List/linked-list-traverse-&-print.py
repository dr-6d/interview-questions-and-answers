


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
    def print(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

ll = LinkedList(Node('a'))
ll.append('b')
ll.append('c')
ll.append('d')
ll.append('e')
ll.append('f')

ll.print()