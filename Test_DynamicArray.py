import unittest

from main import DynamicArray


class MyTestCase(unittest.TestCase):
    def test_pushback(self):
        dynArr = DynamicArray(7)
        dynArr.pushback(1)
        dynArr.pushback(2)
        dynArr.pushback(3)

        actual = []
        for i in range(0, dynArr.getSize()):
            actual.append(dynArr.get(i))

        self.assertEqual([1, 2, 3],  actual)

    def test_pushback_to_undersized_array(self):
        dynArr = DynamicArray(2)
        dynArr.pushback(0)
        dynArr.pushback(1)
        dynArr.pushback(2)

        self.assertEqual(3, dynArr.getSize())
        self.assertEqual(4, dynArr.getCapacity())

    def test_complex_test(self):
        dynArr = DynamicArray(1)
        self.assertEqual(1, dynArr.getCapacity())
        self.assertEqual(0, dynArr.getSize())
        dynArr.pushback(1)
        self.assertEqual(1, dynArr.getCapacity())
        self.assertEqual(1, dynArr.getSize())
        dynArr.pushback(2)
        self.assertEqual(2, dynArr.getCapacity())
        self.assertEqual(2, dynArr.getSize())
        self.assertEqual(2, dynArr.get(1))
        dynArr.set(1, 3)
        self.assertEqual(3, dynArr.get(1))
        self.assertEqual(3, dynArr.popback())
        self.assertEqual(1, dynArr.getSize())
        self.assertEqual(2, dynArr.getCapacity())

    def test_pushback_thrice_pop_twice_get_once(self):
        dynArr = DynamicArray(5)
        dynArr.pushback(1)
        dynArr.pushback(2)
        dynArr.pushback(3)
        self.assertEqual(3, dynArr.popback())
        self.assertEqual(2, dynArr.popback())
        self.assertEqual(1, dynArr.get(0))


    def test_most_complex_case(self):
        dynArr = DynamicArray(1)
        self.assertEqual(0, dynArr.getSize())
        self.assertEqual(1, dynArr.getCapacity())
        for i in range(1, 10):
            dynArr.pushback(i)

        self.assertEqual(9, dynArr.getSize())
        self.assertEqual(16, dynArr.getCapacity())
        for i in range(1, 9):
            dynArr.popback()
        self.assertEqual(1, dynArr.popback())


if __name__ == '__main__':
    unittest.main()
