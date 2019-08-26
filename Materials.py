from typing import Dict
from Recipe import Recipe

basic_materials = ['obsidian', 'diamond', 'redstone', 'iron ingot', 'osmium ingot', 'gold ingot', 'lapis',
                   'cobalt ingot', 'glowstone dust', 'lead ingot', 'coal', 'wood', 'stick', 'cobblestone']


# A class intended to act as a dictionary of recipe
class RecipeDict:
    recipes: Dict[str, Recipe] = {}

    def __init__(self):
        self.set_recipe()

    def set_recipe(self):
        self.recipes = {
            'obsidian dust':
                Recipe('obsidian dust', [['obsidian', 1]], outputs=4),
            'refined obsidian':
                Recipe('refined obsidian', [['obsidian dust', 1], ['diamond', 1]]),
            'ultimate control circuit':
                Recipe('ultimate control circuit', [['atomic alloy', 2], ['elite control circuit', 1]]),
            'elite control circuit':
                Recipe('elite control circuit', [['reinforced alloy', 2], ['advanced control circuit', 1]]),
            'advanced control circuit':
                Recipe('advanced control circuit', [['enriched alloy', 2], ['basic control circuit', 1]]),
            'basic control circuit':
                Recipe('basic control circuit', [['redstone', 1], ['osmium ingot', 1]]),
            'atomic alloy':
                Recipe('atomic alloy', [['refined obsidian', 1], ['reinforced alloy', 1]]),
            'reinforced alloy':
                Recipe('reinforced alloy', [['diamond', 1], ['enriched alloy', 1]]),
            'enriched alloy':
                Recipe('enriched alloy', [['iron ingot', 1], ['redstone', 1]]),
            'teleportation core':
                Recipe('teleportation core', [['lapis', 4], ['gold ingot', 2], ['diamond', 1], ['atomic alloy', 2]]),
            'quantum entangloporter':
                Recipe('quantum entangloporter',
                       [['refined obsidian', 4], ['ultimate control circuit', 2], ['atomic alloy', 2],
                        ['teleportation core', 1]]),
            'modularium':
                Recipe('modularium', [['cobalt ingot', 3], ['redstone', 3], ['glowstone dust', 1], ['lead ingot', 2]],
                       outputs=5),
            'machine casing':
                Recipe('machine casing', [['modularium', 4], ['redstone block', 1]], outputs=2),
            'machine gearbox':
                Recipe('machine gearbox', [['modularium', 4], ['steel gear', 4]]),
            'machine circuitry':
                Recipe('machine circuitry', [['basic control circuit', 4], ['modularium', 4]]),
            'steel gear':
                Recipe('steel gear', [['steel ingot', 4]]),
            'steel ingot':
                Recipe('steel ingot', [['coal', 6], ['iron ingot', 2]], 2),
            'iron block':
                Recipe('iron block', [['iron ingot', 9]]),
            'redstone block':
                Recipe('redstone block', [['redstone', 9]]),
            'mob masher':
                Recipe('mob masher', [['iron sword', 2], ['diamond', 3], ['iron block', 1], ['iron spikes', 2],
                                      ['redstone block', 1]]),
            'iron spikes':
                Recipe('iron spikes', [['iron sword', 3], ['iron block', 1]]),
            'iron sword':
                Recipe('iron sword', [['stick', 1], ['iron ingot', 2]]),
            'tiny energy input':
                Recipe('tiny energy input', [['redstone', 3], ['redstone block', 1], ['machine casing', 1],
                                             ['redstone repeater', 2]]),
            'redstone repeater':
                Recipe('redstone repeater', [['cobblestone', 3], ['stick', 2], ['redstone', 3]]),
            'tiny item input':
                Recipe('tiny item input', [['chest', 1], ['hopper', 1], ['machine casing', 1]]),
            'tiny item output':
                Recipe('tiny item output', [['chest', 1], ['hopper', 1], ['machine casing', 1]]),
            'chest':
                Recipe('chest', [['wood', 8]]),
            'hopper':
                Recipe('hopper', [['chest', 1], ['iron ingot', 5]]),
            'machine controller':
                Recipe('machine controller', [['diamond',  1], ['redstone block', 3], ['gold ingot', 2],
                                              ['machine casing', 1]]),
            'auto sieve':
                Recipe('auto sieve', [['machine casing', 59], ['machine gearbox', 16], ['machine circuitry', 4],
                                      ['tiny item input', 2], ['tiny item output', 2], ['tiny energy input', 2],
                                      ['iron block', 12], ['mob masher', 1], ['machine controller', 1]])
        }

    def __getitem__(self, item):
        return self.recipes[item]

    def __setitem__(self, key, value):
        self.recipes[key] = value
        return

    def __contains__(self, item):
        return item in self.recipes

    def __len__(self):
        return len(self.recipes)

    def __str__(self):
        return str(self.recipes)

    def __iter__(self):
        return self.recipes.__iter__()

    def update(self, inputs: Dict):
        self.recipes.update(inputs)
        return

    def items(self):
        return self.recipes.items()


class CompressionRecipeDict(RecipeDict):

    def set_recipe(self):
        self.recipes = {
            'iron ingot': ['iron block', 9],
            'coal': ['coal block', 9],
            'redstone': ['redstone block', 9],
            'cobalt ingot': ['cobalt block', 9],
            'diamond': ['diamond block', 9],
            'osmium ingot': ['osmium block', 9],
            'lapis': ['lapis block', 9],
            'gold ingot': ['gold block', 9],
            'lead ingot': ['lead block', 9],
            'cobblestone': ['compressed cobblestone', 9]
        }
