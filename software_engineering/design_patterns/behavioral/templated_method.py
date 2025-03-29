class Game:
    def play(self):
        return f"{self.initialize()} {self.start()} {self.end()}"

    def initialize(self):
        return "Game initialized"

    def start(self):
        pass

    def end(self):
        pass

class Chess(Game):
    def start(self):
        return "Chess started"

    def end(self):
        return "Chess ended"

class Soccer(Game):
    def start(self):
        return "Soccer started"

    def end(self):
        return "Soccer ended"

chess = Chess()
print(chess.play())
soccer = Soccer()
print(soccer.play())