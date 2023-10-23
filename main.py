class DynamicArray:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = [None] * capacity

    def get(self, i: int) -> int:
        index = self.findTrueIndexAtIndex(i)
        value = self.data[index]
        return value

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
        index = self.findTrueIndexAtIndex(i)
        self.data[index] = n

    def pushback(self, n: int) -> None:
        if self.getSize() == self.getCapacity():
            self.resize()

        reverseIndex = self.findFirstElementReverse(None, 0)

        self.data[reverseIndex] = n
        data_to_shift = self.data[reverseIndex + 1:]
        self.data = self.data[:reverseIndex]
        self.data += data_to_shift
        self.data.append(n)

    def findFirstElementReverse(self, element=None, comparator=0):
        def comparison_function(value):
            return value == element if comparator == 0 else value != element

        index = 0
        reverseIndex = -1

        while True:
            reverseIndex = len(self.data) - 1 - index
            value = self.data[reverseIndex]
            if reverseIndex < 0 or comparison_function(self.data[reverseIndex]):
                return reverseIndex  # This will return -1 if no element is found, adjust as needed.
            index += 1

        return reverseIndex

    def popback(self) -> int:
        reverseIndex = self.findFirstElementReverse(None, 1)
        value = self.data[reverseIndex]
        self.data[reverseIndex] = None
        return value

    def resize(self) -> None:
        temp = self.data
        self.data = [None] * len(temp) * 2

        for index, element in enumerate(temp):
            self.data[index] = element

    def getSize(self) -> int:
        size = 0
        for elem in self.data:
            if elem is not None:
                size += 1

        return size

    def getCapacity(self) -> int:
        return len(self.data)
