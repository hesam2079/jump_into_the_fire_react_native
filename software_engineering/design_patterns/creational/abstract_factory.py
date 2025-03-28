class Button:
    def render(self): pass

class WindowsButton(Button):
    def render(self): return "Windows Button"

class MacButton(Button):
    def render(self): return "Mac Button"

class GUIFactory:
    def create_button(self): pass

class WindowsFactory(GUIFactory):
    def create_button(self): return WindowsButton()

class MacFactory(GUIFactory):
    def create_button(self): return MacButton()


factory = WindowsFactory()
button = factory.create_button()
print(button.render())