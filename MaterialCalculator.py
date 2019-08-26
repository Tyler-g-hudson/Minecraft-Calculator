import sys, math
from typing import Dict, List
from Materials import RecipeDict, basic_materials, CompressionRecipeDict
from WorkTree import Dependency, RecipeDependency, DependencyDict


def get_raw_mats(key: str, quantity: int):

    recipes: RecipeDict = RecipeDict()
    key_adjusted = key.lower()

    if key_adjusted in basic_materials:
        return [key_adjusted, quantity]
    elif key_adjusted not in recipes:
        print("ERROR: Recipe not found: " + key)
        return

    prime_dependency = RecipeDependency(recipes[key_adjusted], key_adjusted, dependencies=0)
    prime_dependency.order(quantity)
    dependency_list = DependencyDict()
    dependency_list.update({key_adjusted: prime_dependency})

    worklist = [key_adjusted]
    cycle_finished = False

    while not cycle_finished:
        cycle_finished = True
        next_worklist = []
        for wl_item in worklist:
            wl_recipe = recipes[wl_item]
            for item in wl_recipe:
                item_name = item[0]
                if item_name in dependency_list:
                    dependency_list[item_name].increment_dependencies()
                else:
                    if item_name in basic_materials:
                        dep = Dependency(item_name)
                    elif item_name in recipes:
                        cycle_finished = False
                        recipe = recipes[item_name]
                        dep = RecipeDependency(recipe, item_name)
                        if item_name not in next_worklist:
                            next_worklist.append(item_name)
                    else:
                        print("ERROR: Recipe not found. Terminating.")
                        sys.exit()
                    dependency_list.update({item_name: dep})
        worklist = next_worklist

    raw_mats: Dict[str, int] = dict()
    cycle_finished = False

    while not cycle_finished:
        dependencies_this_cycle: List[Dependency] = []
        for dependency_name in dependency_list:
            dep = dependency_list[dependency_name]
            if dep.dependencies() == 0:
                dependencies_this_cycle.append(dep)

        for dep in dependencies_this_cycle:
            dep_quantity = dep.quantity()
            dep_name = dep.name()

            if type(dep) == RecipeDependency:
                recipe = dep.__getattribute__('recipe')
                for item in recipe:
                    item_name = item[0]
                    item_recipe_quantity = item[1]
                    item_dep = dependency_list[item_name]
                    recipe_reps = math.ceil(dep_quantity * item_recipe_quantity / recipe.outputs)
                    item_dep.order(recipe_reps)
                    item_dep.decrement_dependencies()

            elif type(dep) == Dependency:
                raw_mats.update({dep_name: dep.quantity()})
            dependency_list.remove(dep_name)

        if dependency_list.is_empty():
            cycle_finished = True

    return raw_mats


def compress_inputs(inputs: Dict[str, int]):
    compressors = CompressionRecipeDict()

    worklist = []
    for item in inputs:
        if item in compressors:
            if inputs[item] > 128:
                worklist.append([item, inputs[item]])

    for item in worklist:
        item_name = item[0]
        item_quantity = item[1]
        compressor_recipe = compressors[item_name]
        compressed_item_name = compressor_recipe[0]
        compression_factor = compressor_recipe[1]

        output_quantity = int(item_quantity / compression_factor)
        remainder = item_quantity % compression_factor
        if remainder == 0:
            del inputs[item_name]
        else:
            inputs.update({item_name: remainder})
        inputs.update({compressed_item_name: output_quantity})

