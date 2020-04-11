import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Lists():
    def __init__(self):
        self.head = None

    def is_empty(self):
        if not self.head:
            return True

    def insertAtLast(self, newdata):
        newnode = Node(newdata)

        if self.is_empty():
            self.head = newnode
            return

        headval = self.head

        while headval.next is not None:
            headval = headval.next

        headval.next = newnode
        newnode.prev = headval
        #headval.prev = headval

    def insertAtBeginning(self, newdata):

        newnode = Node(newdata)

        if self.is_empty():
            self.head = newnode
            return

        headval = self.head

        # while headval.prev is not None:
        #     headval = headval.next

        # headval.prev = newnode
        # newnode.next = headval

        newnode.next = headval
        headval.prev = newnode
        self.head = newnode

    def insertAfter(self, x_data, newdata):

        newnode = Node(newdata)

        if self.is_empty():
            print("List is empty")
            return

        # TODO: insert after node x
        headval = self.head

        while headval is not None:

            if headval.data == x_data:
                break

            headval = headval.next

        if headval is None: return print("can't find item, sorry.")
        else:
            newnode.prev = headval
            newnode.next = headval.next

            if headval.next is not None:
                headval.next.prev = newnode

        headval.next = newnode

    def insertBefore(self, x_data, newdata):
        pass

    def deleteFirst(self):
        pass

    def deleteLast(self):
        if self.is_empty(): return print("list is empty, nothing to delete.")

        #if the node has no next node, return empty
        if self.head.next is None:
            self.head = None
            return

        headval = self.head
        while headval.next is not None:
            headval = headval.next

        headval.prev.next = None

    #TODO: revisar
    def deleteActual(self, x_data):
        """ Deletes a specific given node from the list.

            :arg
            Deletes the node from the list.
        """

        if self.is_empty():
            return print("List is empty. Nothing to show.")

        headval = self.head

        while headval is not None:
            if headval.data == x_data:
                break

            headval = headval.next

        if headval is None:
            return print("can't find item. sorry.")

        if headval.next is not None:
            headval.next.prev = headval.prev
            headval.prev.next = headval.next
        else:
            headval.prev.next = headval.next # will point to default null



    def displayForward(self):
        pass

    def displayBackward(self):
        pass





List = Lists()

List.insertAtLast("Uno")
List.insertAtLast("Dos")
List.insertAtLast("Tres")
List.deleteActual("Dos")

List.deleteLast()

a = "The new one"

def holis():
    pass