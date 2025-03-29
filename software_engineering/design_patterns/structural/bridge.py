class DrawingAPI:
    def draw_circle(self, radius):
        pass

class DrawingAPI1(DrawingAPI):
    def draw_circle(self, radius):
        return f"API1 drawing circle with radius {radius}"

class DrawingAPI2(DrawingAPI):
    def draw_circle(self, radius):
        return f"API2 drawing circle with radius {radius}"

class Circle:
    def __init__(self, radius, drawing_api):
        self.radius = radius
        self.drawing_api = drawing_api

    def draw(self):
        return self.drawing_api.draw_circle(self.radius)

circle1 = Circle(5, DrawingAPI1())
circle2 = Circle(10, DrawingAPI2())
print(circle1.draw())
print(circle2.draw())