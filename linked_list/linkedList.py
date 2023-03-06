# Define the node of one-way linked list
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# Define the node of double linked list
class DoubleListNode:
    def __init__(self, val: int):
        self.val = val
        self.prev = None
        self.next = None


class LinkedList:
    """
    Define one-way linked list from https://leetcode.cn/problems/design-linked-list/solution/she-ji-lian-biao-by-leetcode/
    """
    def __init__(self):
        self.size = 0
        # Sentinel node as pseudo-head
        self._head = ListNode(0)


    def __repr__(self):
        """
        Returns the normalized string representation
        """
        currNode = self._head
        # Notice that the first node is pseudo-head, don't need to read it
        res = []
        while currNode.next != None:
            currNode = currNode.next
            res.append(currNode.val)
            
        return "LinkedList({})".format(res)


    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size:
            return -1
        currNode = self._head
        for _ in range(index + 1):
            currNode = currNode.next

        return currNode.val


    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)


    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)


    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        """
        if index > self.size:
            return
        if index < 0:
            index = 0
        currNode = self._head
        # Need index steps to move to the insert position before
        for _ in range(index):
            currNode = currNode.next
        toAdd = ListNode(val)
        toAdd.next = currNode.next
        currNode.next = toAdd
        self.size += 1


    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list if the index is valid.
        """
        if index < 0 or index >= self.size:
            return
        currNode = self._head
        # Need index steps to move to the delete position before
        for _ in range(index):
            currNode = currNode.next
        currNode.next = currNode.next.next
        self.size -= 1


class DoubleLinkedList():
    def __init__(self):
        self.size = 0
        self._head = DoubleListNode(0)
        self._tail = DoubleListNode(0)
        self._head.next = self._tail
        self._tail.prev = self._head
    

    def __repr__(self):
        """
        Returns the normalized string representation
        """
        currNode = self._head
        # Notice that the first node is pseudo-head, don't need to read it
        res = []
        while currNode.next != self._tail:
            currNode = currNode.next
            res.append(currNode.val)
        return "DoubleLinkedList({})".format(res)


    def __getNode(self, index: int) -> DoubleListNode:
        """
        Get the index-th node in the double linked list.
        """
        if index < self.size // 2:
            currNode = self._head
            for _ in range(index + 1):
                currNode = currNode.next
            return currNode
        else:
            currNode = self._tail
            for _ in range(self.size - index):
                currNode = currNode.prev
            return currNode


    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the double linked list.
        If the index is invalid(small than 0 or big than the length of linked list), return -1.
        """
        if index < 0 or index >= self.size:
            return -1
        indexNode = self.__getNode(index)
        return indexNode.val
    

    def addAtHead(self, val: int):
        """
        Add a node of value val before the first element of the double linked list.
        After the insertion, the new node will be the first node of the double linked list.
        """
        self.addAtIndex(0, val)


    def addAtTail(self, val: int):
        """
        Add a node of value val after the last element of the double linked list.
        Adter the insertion, the new node will be the last node of the double linked list.
        """
        self.addAtIndex(self.size, val)


    def addAtIndex(self, index: int, val: int):
        """
        Add a node of value val before the index-th node in the double linked list.
        If index equals to the length of double linked list, the node will be appended to the end of double linked list.
        If index is greater that the length, the node will not be inserted.
        """
        if index > self.size:
            return
        if index < 0:
            index = 0
        indexNode = self.__getNode(index)
        toAddNode = DoubleListNode(val)
        toAddNode.next = indexNode
        toAddNode.prev = indexNode.prev
        indexNode.prev = toAddNode
        toAddNode.prev.next = toAddNode
        self.size += 1


    def deleteAtIndex(self, index: int):
        """
        Delete the index-th node in the double linked list if the index is valid.
        """
        if index < 0 or index >= self.size:
            return
        toDeleteNode = self.__getNode(index)
        toDeleteNode.prev.next = toDeleteNode.next
        toDeleteNode.next.prev = toDeleteNode.prev
        self.size -= 1