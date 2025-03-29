class NumberCollection:
    def __init__(self):
        self.numbers = [1, 2, 3, 4, 5]

    def __iter__(self):
        return NumberIterator(self.numbers)

class NumberIterator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0

    def __next__(self):
        if self.index < len(self.numbers):
            result = self.numbers[self.index]
            self.index += 1
            return result
        raise StopIteration

collection = NumberCollection()
for num in collection:
    print(num)