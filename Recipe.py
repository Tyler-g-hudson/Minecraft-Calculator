from typing import Dict


class Recipe:
    item: str = ''
    inputs: Dict[str, int] = []
    outputs: int = 1

    def __init__(self, item: str, inputs, outputs=1):
        self.item = item
        self.inputs = inputs
        self.outputs = outputs
        return

    def __getitem__(self, item):
        return self.inputs[item]

    def __iter__(self):
        return self.inputs.__iter__()