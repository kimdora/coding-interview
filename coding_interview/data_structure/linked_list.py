class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.num_of_nodes = 0

    def insert_first(self, data: int):
        new_node = Node(data, None)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_of_nodes += 1
    
    def insert_last(self, data: int):
        new_node = Node(data, None)
        if self.head == None:
            self.head = new_node
        else:
            cur = Node(data, None)
            while cur.next != None:
                cur = cur.next
            cur.next = new_node
        self.num_of_nodes += 1

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_first(3)
    ll.insert_last(7)
    ll.insert_first(1)
    ll.insert_last(5)
    
    

