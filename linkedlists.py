class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.start = None

    def insert(self, new_value):
        NewNode = Node(new_value)
        if self.start == None:#tylko przy pierwszym wywołaniu insert
            self.start = NewNode
            return
        #print(self.start.value, self.start.next)
        current = self.start#ale next cały czas już mam
        while current.next != None:#przesuwają się dołączone węzły aż next==None
            current = current.next

        current.next = NewNode#dopisuje do węzła nowy węzeł


    def print(self):
        current = self.start#bieżący węzeł to 10, a next to 20 itd.
        while current is not None:
            print(current.value)
            current = current.next


lista = LinkedList()
lista.insert(10)
lista.insert(20)
lista.insert(30)
lista.insert(40)
lista.insert(50)
lista.print()

lista.insert(40)
lista.print()
