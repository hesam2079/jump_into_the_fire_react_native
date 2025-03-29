class Light:
    def on(self):
        return "Light is ON"

    def off(self):
        return "Light is OFF"

class Command:
    def execute(self):
        pass

class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        return self.light.on()

class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        return self.light.off()

class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        return self.command.execute()

light = Light()
remote = RemoteControl()
remote.set_command(LightOnCommand(light))
print(remote.press_button())
remote.set_command(LightOffCommand(light))
print(remote.press_button())