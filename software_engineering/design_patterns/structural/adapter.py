class EuropeanPlug:
    def provide_power(self):
        return "220V"

class USSocket:
    def accept_power(self, voltage):
        return f"US Socket received {voltage}"

class Adapter:
    def __init__(self, plug):
        self.plug = plug

    def convert(self):
        return self.plug.provide_power()

european_plug = EuropeanPlug()
adapter = Adapter(european_plug)
socket = USSocket()
print(socket.accept_power(adapter.convert()))