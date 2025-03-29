class Subject:
    def __init__(self):
        self.observers = []
        self.state = 0

    def attach(self, observer):
        self.observers.append(observer)

    def set_state(self, state):
        self.state = state
        self.notify()

    def notify(self):
        for observer in self.observers:
            observer.update(self.state)

class Observer:
    def update(self, state):
        pass

class Display(Observer):
    def update(self, state):
        return f"Display updated with state: {state}"

subject = Subject()
display = Display()
subject.attach(display)
subject.set_state(42)
print(display.update(subject.state))