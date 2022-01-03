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
    def length(self):
        count = 0;
        temp = self.head
        while temp:
            temp = temp.next        
            count += 1
        return count
    def fetchNode(self, index):
        # variableLength = self.length()
        if (self.length() - index) < 0:
            return "negative index error"
        else:
            temp = self.head
            for i in range(self.length() - index):
                if temp:
                    temp = temp.next
                else:
                    return 'index out of range'
        return temp.data

ll = LinkedList(Node('a'))
ll.append('b')
ll.append('c')
ll.append('d')
ll.append('e')
ll.append('f')
print(ll.fetchNode(-5))
print(ll.fetchNode(3))
print(ll.fetchNode(10))