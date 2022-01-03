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
    def sumOfList(self):
        sum = 0
        temp = self.head
        while temp:
            sum += temp.data
            temp = temp.next
        return sum

ll = LinkedList(Node(1))
ll.append(2)
ll.append(4)
ll.append(6)
ll.append(22)
print(ll.sumOfList())