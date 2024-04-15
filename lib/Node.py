class Node:
    
    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node

    # def __repr__(self)

bulldog = Node("Bulldog")

chihuahua =Node("Chihuahua")
bulldog.next_node = chihuahua

german_shepherd = Node("German Shepherd")
chihuahua.next_node = german_shepherd

retriever = Node("Retriever")
german_shepherd.next_node = retriever

shiba_inu = Node("Shiba Inu")

class LinkedList:
    
    def __init__(self, head = None):
        self.head = head

    def __repr__(self):
        return (f"{self} and {self.head}")

    def append(self, node):
        # add element to beginning of the list if the list is mt
        if self.head == None:
            self.head = node
            return
        # otherwise, traverse the list to find the last node 
        last_node = self.head
        while last_node.next_node:
        # and add the node to the end
            last_node.next_node = node

    list = list()

    list.append(Node("Bulldog"))
    list.append(Node("Chihuahua"))
    list.append(Node("German Shepherd"))

    print(list)
