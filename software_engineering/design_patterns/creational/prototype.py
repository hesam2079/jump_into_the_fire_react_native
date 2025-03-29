import copy

class Note:
    def __init__(self):
        self.pitch = "C"
        self.duration = "Quarter"

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"Pitch: {self.pitch}, Duration: {self.duration}"

original = Note()
clone = original.clone()
clone.pitch = "G"
print(original)
print(clone)