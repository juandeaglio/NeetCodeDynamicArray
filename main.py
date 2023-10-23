class DynamicArray:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = [None] * capacity
        self.size = 0

    def get(self, i: int) -> int:
        return self.data[i]

    def set(self, i: int, n: int) -> None:
        self.data[i] = n

    def pushback(self, n: int) -> None:
        if self.getSize() == self.getCapacity():
            self.resize()

        self.data[self.size] = n
        self.size += 1

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
