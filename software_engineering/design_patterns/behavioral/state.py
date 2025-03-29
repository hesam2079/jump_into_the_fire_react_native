class State:
    def handle(self):
        pass

class OffState(State):
    def handle(self):
        return "Light is OFF"

class OnState(State):
    def handle(self):
        return "Light is ON"

class LightSwitch:
    def __init__(self):
        self.state = OffState()

    def set_state(self, state):
        self.state = state

    def operate(self):
        return self.state.handle()

light = LightSwitch()
print(light.operate())
light.set_state(OnState())
print(light.operate())