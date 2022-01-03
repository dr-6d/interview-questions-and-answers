# RETURNS THE VALUE OF THE nth NODE 
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
    def fetchNode(self, index):
        temp = self.head
        for i in range(index):
            if temp:
                temp = temp.next
            else:
                return 'index error'
        return temp.data

ll = LinkedList(Node('a'))
ll.append('b')
ll.append('c')
ll.append('d')
ll.append('e')
ll.append('f')
print(ll.fetchNode(7))
print(ll.fetchNode(3))
