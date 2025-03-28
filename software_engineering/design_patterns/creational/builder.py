class Document:
    def __init__(self):
        self.content = []

    def add(self, text):
        self.content.append(text)

    def __str__(self):
        return "\n".join(self.content)

class TextBuilder:
    def __init__(self):
        self.doc = Document()

    def add_header(self, text):
        self.doc.add(f"Header: {text}")
        return self

    def add_body(self, text):
        self.doc.add(f"Body: {text}")
        return self

    def build(self):
        return self.doc

builder = TextBuilder()
doc = builder.add_header("Title").add_body("Hello World").build()
print(doc)