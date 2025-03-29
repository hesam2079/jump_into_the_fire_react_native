class Strategy:
    def sort(self, data):
        pass

class QuickSort(Strategy):
    def sort(self, data):
        return sorted(data)

class MergeSort(Strategy):
    def sort(self, data):
        return sorted(data, reverse=True)

class Sorter:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def sort(self, data):
        return self.strategy.sort(data)

sorter = Sorter(QuickSort())
print(sorter.sort([3, 1, 4]))
sorter.set_strategy(MergeSort())
print(sorter.sort([3, 1, 4]))