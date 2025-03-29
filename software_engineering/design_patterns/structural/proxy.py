class Image:
    def display(self):
        pass

class RealImage(Image):
    def __init__(self, filename):
        self.filename = filename

    def display(self):
        return f"Displaying {self.filename}"

class ProxyImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.real_image = None

    def display(self):
        if self.real_image is None:
            self.real_image = RealImage(self.filename)
        return self.real_image.display()

image = ProxyImage("photo.jpg")
print(image.display())
print(image.display())