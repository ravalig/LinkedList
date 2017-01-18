class Element(object):
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if(self.head):
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def value_at_position(self,position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        current = self.head
        counter = 1
        while current and counter<=position:
            if position == counter:
                return current.value
            current = current.next
            counter += 1
        return None

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        current = self.head
        counter = 1
        if position > 1:
            while current and counter <= position:
                if (position -1) == counter:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter += 1
                elif position == 1:
                    new_element.next = self.head
                    self.head = new_element

    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next



e1 = Element("Red")
e2 = Element("Green")
e3 = Element("Blue")
e4 = Element("Yellow")
e5 = Element("Orange")

LL = LinkedList(e1)
LL.append(e2)
