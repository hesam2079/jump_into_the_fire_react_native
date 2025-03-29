class Memento:
    def __init__(self, state):
        self.state = state

class Editor:
    def __init__(self):
        self.content = ""

    def type(self, words):
        self.content += words

    def save(self):
        return Memento(self.content)

    def restore(self, memento):
        self.content = memento.state

    def get_content(self):
        return self.content

editor = Editor()
editor.type("Hello ")
memento = editor.save()
editor.type("World")
print(editor.get_content())
editor.restore(memento)
print(editor.get_content())