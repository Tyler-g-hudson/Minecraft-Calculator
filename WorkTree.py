from Recipe import Recipe
from typing import Dict


class Dependency:
    item: str = ''
    unprocessed_dependencies: int = 1
    quant: int = 0

    def __init__(self, item_name: str, dependencies=1):
        self.item = item_name
        self.unprocessed_dependencies = dependencies
        return

    def __str__(self):
        return "Dependency: " + self.item + " with " + str(self.unprocessed_dependencies) + " unprocessed dependencies."

    def __repr__(self):
        return str(self)

    def increment_dependencies(self):
        self.unprocessed_dependencies += 1

    def decrement_dependencies(self):
        self.unprocessed_dependencies -= 1

    def dependencies(self):
        return self.unprocessed_dependencies

    def name(self):
        return self.item

    def quantity(self):
        return self.quant

    def order(self, quantity: int):
        self.quant += quantity


class RecipeDependency(Dependency):
    recipe: Recipe = ''

    def __init__(self, recipe: Recipe, item_name: str, dependencies=1):
        self.recipe = recipe
        Dependency.__init__(self, item_name, dependencies)
        return

    def __str__(self):
        return "RecipeDependency: " + self.item + " with " + str(self.unprocessed_dependencies) \
               + " unprocessed dependencies."


class DependencyDict:
    dependencies: Dict[str, Dependency] = dict()

    def __getitem__(self, item):
        return self.dependencies[item]

    def __setitem__(self, key, value):
        self.dependencies[key] = value
        return

    def __contains__(self, item):
        return item in self.dependencies

    def __len__(self):
        return len(self.dependencies)

    def __str__(self):
        return str(self.dependencies)

    def __iter__(self):
        return self.dependencies.__iter__()

    def update(self, inputs: Dict):
        self.dependencies.update(inputs)
        return

    def items(self):
        return self.dependencies.items()

    def is_empty(self):
        return len(self.dependencies) == 0

    def remove(self, item):
        del self.dependencies[item]
