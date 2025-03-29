class Handler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle(self, request):
        pass

class LowLevelHandler(Handler):
    def handle(self, request):
        if request <= 10:
            return f"LowLevelHandler handled {request}"
        elif self.successor:
            return self.successor.handle(request)

class HighLevelHandler(Handler):
    def handle(self, request):
        if request > 10:
            return f"HighLevelHandler handled {request}"
        elif self.successor:
            return self.successor.handle(request)

handler = LowLevelHandler(HighLevelHandler())
print(handler.handle(5))
print(handler.handle(15))