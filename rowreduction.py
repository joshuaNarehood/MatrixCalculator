class Item:
    def __init__(self, value):
        self.value = value
        self.next = None

class Row:
    def __init__(self, lst):
        self.head = Item(lst[0])
        self.value = lst
        self.below = None
        self.addItems(lst[1:])

    def addItems(self, lst):
        placeHolder = self.head
        for value in lst:
            item = Item(value)
            placeHolder.next = item
            placeHolder = placeHolder.next
        
        return None

class Matrix:
    def __init__(self, lsts):
        self.rowHead = Row(lsts[0])
        self.addRows(lsts[1:])

    def addRows(self,lsts):
        placeHolder = self.rowHead
        for lst in lsts:
            row = Row(lst)
            placeHolder.below = row
            placeHolder = placeHolder.below
        
        return None