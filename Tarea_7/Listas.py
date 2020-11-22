class DoubleNode:
    def __init__(self, value = None, next = None, prev = None):
        self.data = value
        self.next = next
        self.prev = prev

class DoubleLinkedList:
    def __init__(self):
        self.__head = DoubleNode()
        self.__tail = DoubleNode()
        self.__head.next = self.__tail
        self.__tail.prev = self.__head
        self.__size = 0
        #print(f"Head: {self.__head}")
        #print(f"Tail: {self.__tail}")

    def is_empty( self ):
        return self.__head.data == None and self.__tail.data==None

    def get_size( self ): #Regresa el numero de elementos en la lista
        return self.__size

    def append( self , value ):
        self.__size+=1
        nuevo=DoubleNode(value)
        if self.is_empty():
            self.__head = DoubleNode(value=value)
            self.__tail=self.__head
        else:
            curr_node = self.__head
            while curr_node.next != None:
                curr_node = curr_node.next
            nuevo=DoubleNode(value=value , prev=curr_node)
            curr_node.next = nuevo
            self.__tail = nuevo

    def find_from_tail(self , value):
        curr_node=self.__tail
        count=0
        while curr_node.data != value:
            curr_node= curr_node.prev
            count += 1
        return count

    def find_from_head(self , value):
        curr_node=self.__head
        count=0
        while curr_node.data != value:
            curr_node= curr_node.next
            count += 1
        return count

    def remove_from_tail(self, value):
        self.__size-=1
        if self.__tail.data == value:
            self.__tail = self.__tail.prev
            self.__tail.next = None
        else:
            curr_node = self.__tail
            while curr_node.data != value and curr_node.prev != None:
                curr_node = curr_node.prev
            if curr_node.data == value:
                curr_node.prev.next = curr_node.next
                curr_node.next.prev = curr_node.prev
            else:
                self.__size+=1
                print("Item not found")

    def remove_from_head(self, value):
        self.__size-=1
        if self.__tail.data == value:
            self.__tail = self.__tail.prev
            self.__tail.next = None
        else:
            curr_node = self.__head
            while curr_node.data != value and curr_node.next != None:
                curr_node = curr_node.next
            if curr_node.data == value:
                curr_node.prev.next = curr_node.next
                curr_node.next.prev = curr_node.prev
            else:
                self.__size+=1
                print("Item not found")

    def transversal( self ):
        curr_node = self.__head
        while curr_node != None:
            print(f" { curr_node.data } -> " , end="")
            curr_node = curr_node.next
        print(" ")

    def reverse_transversal( self ):
        curr_node = self.__tail
        while curr_node != None:
            print(f" { curr_node.data } -> " , end="")
            curr_node = curr_node.prev
        print(" ")
