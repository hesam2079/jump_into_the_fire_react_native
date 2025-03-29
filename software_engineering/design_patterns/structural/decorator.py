class Text:
    def render(self):
        pass

class PlainText(Text):
    def render(self):
        return "Hello"

class BoldText(Text):
    def __init__(self, text):
        self.text = text

    def render(self):
        return f"<b>{self.text.render()}</b>"

class ItalicText(Text):
    def __init__(self, text):
        self.text = text

    def render(self):
        return f"<i>{self.text.render()}</i>"

text = PlainText()
bold_text = BoldText(text)
italic_bold_text = ItalicText(bold_text)
print(text.render())
print(bold_text.render())
print(italic_bold_text.render())