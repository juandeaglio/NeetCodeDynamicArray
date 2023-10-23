class DynamicArray:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = [None] * capacity
        self.size = 0

    def get(self, i: int) -> int:
        return self.data[i]

    def findTrueIndexAtIndex(self, i):

        count = 0
        index = 0
        while index < self.getCapacity():
            if self.data[index] is not None:
                count += 1
                if i + 1 == count:
                    return index

            index += 1

    def set(self, i: int, n: int) -> None:
        self.data[i] = n

    def pushback(self, n: int) -> None:
        if self.getSize() == self.getCapacity():
            self.resize()

        self.data[self.size] = n
        self.size += 1


    def findFirstElementReverse(self, element=None, comparator=0):

        def comparison_function(value):
            return value == element if comparator == 0 else value != element

        index = 0
        reverseIndex = -1

        while True:
            reverseIndex = len(self.data) - 1 - index
            value = self.data[reverseIndex]
            if reverseIndex < 0 or comparison_function(self.data[reverseIndex]):
                return reverseIndex
            index += 1

    def popback(self) -> int:
        self.size -= 1
        value = self.data[self.size]
        self.data[self.size] = None
        return value

    def resize(self) -> None:
        temp = self.data
        self.capacity = len(temp) * 2
        self.data = [None] * self.capacity

        for index, element in enumerate(temp):
            self.data[index] = element

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity
