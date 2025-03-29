class Mediator:
    def notify(self, sender, event):
        pass

class ChatRoom(Mediator):
    def notify(self, sender, event):
        return f"{sender.name} says: {event}"

class User:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator

    def send(self, message):
        return self.mediator.notify(self, message)

chat = ChatRoom()
user1 = User("Alice", chat)
user2 = User("Bob", chat)
print(user1.send("Hi Bob!"))
print(user2.send("Hi Alice!"))