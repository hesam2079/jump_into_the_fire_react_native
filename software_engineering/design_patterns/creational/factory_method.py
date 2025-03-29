class Shape:
    def draw(self): pass

class Line(Shape):
    def draw(self): return "Drawing a Line"

class Circle(Shape):
    def draw(self): return "Drawing a Circle"

class ShapeCreator:
    def create_shape(self): pass

class LineCreator(ShapeCreator):
    def create_shape(self): return Line()

class CircleCreator(ShapeCreator):
    def create_shape(self): return Circle()


creator = CircleCreator()
shape = creator.create_shape()
print(shape.draw())