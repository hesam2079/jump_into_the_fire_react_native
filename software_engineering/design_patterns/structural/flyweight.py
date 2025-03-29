class TreeType:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def draw(self, x, y):
        return f"Drawing {self.name} ({self.color}) at ({x}, {y})"

class TreeFactory:
    tree_types = {}

    @staticmethod
    def get_tree_type(name, color):
        key = (name, color)
        if key not in TreeFactory.tree_types:
            TreeFactory.tree_types[key] = TreeType(name, color)
        return TreeFactory.tree_types[key]

tree1 = TreeFactory.get_tree_type("Pine", "Green")
tree2 = TreeFactory.get_tree_type("Pine", "Green")
print(tree1.draw(10, 20))
print(tree2.draw(30, 40))
print(tree1 is tree2)