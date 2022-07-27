class singleLL:
    def __init__(self):
        self.head = None
        self.tail = None


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


SingalyLL = singleLL()
node1 = Node(1)
print(node1)
node2 = Node(2)
print(node2)

SingalyLL.head = node1
print(SingalyLL.head)
SingalyLL.head.next = node2
print(SingalyLL.head.next)
SingalyLL.tail = node2
print(SingalyLL.tail)
