class Graphic:
    def draw(self):
        pass

class Line(Graphic):
    def draw(self):
        return "Drawing Line"

class Rectangle(Graphic):
    def draw(self):
        return "Drawing Rectangle"

class Picture(Graphic):
    def __init__(self):
        self.children = []

    def add(self, graphic):
        self.children.append(graphic)

    def draw(self):
        result = ["Picture ["]
        for child in self.children:
            result.append(child.draw())
        result.append("]")
        return " ".join(result)

picture = Picture()
picture.add(Line())
picture.add(Rectangle())
print(picture.draw())