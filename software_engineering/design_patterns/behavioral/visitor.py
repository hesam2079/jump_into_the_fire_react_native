class Element:
    def accept(self, visitor):
        pass

class Book(Element):
    def __init__(self, price):
        self.price = price

    def accept(self, visitor):
        return visitor.visit_book(self)

class Fruit(Element):
    def __init__(self, price):
        self.price = price

    def accept(self, visitor):
        return visitor.visit_fruit(self)

class Visitor:
    def visit_book(self, book):
        pass

    def visit_fruit(self, fruit):
        pass

class PriceVisitor(Visitor):
    def visit_book(self, book):
        return f"Book price: {book.price}"

    def visit_fruit(self, fruit):
        return f"Fruit price: {fruit.price}"

book = Book(10)
fruit = Fruit(5)
visitor = PriceVisitor()
print(book.accept(visitor))
print(fruit.accept(visitor))