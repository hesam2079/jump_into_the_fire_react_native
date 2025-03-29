class CPU:
    def process(self):
        return "CPU processing"

class Memory:
    def load(self):
        return "Memory loading"

class HardDrive:
    def read(self):
        return "Hard Drive reading"

class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()

    def start(self):
        return [self.cpu.process(), self.memory.load(), self.hard_drive.read()]

computer = ComputerFacade()
print(" ".join(computer.start()))