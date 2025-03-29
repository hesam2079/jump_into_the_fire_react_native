class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.logs = []
        return cls._instance

    def log(self, message):
        self.logs.append(message)

    def __str__(self):
        return "\n".join(self.logs)

logger1 = Logger()
logger1.log("Error 1")
logger2 = Logger()
logger2.log("Error 2")
print(logger1)
print(logger1 is logger2)