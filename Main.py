import math
import MaterialCalculator


input_item = ('auto sieve')
quantity = 1
input_dict = MaterialCalculator.get_raw_mats(input_item, 1)
MaterialCalculator.compress_inputs(input_dict)

print("Inputs required for: " + input_item + " x" + str(quantity))
for key in sorted(input_dict.keys()):
    print('\t' + key + ': ' + str(math.ceil(input_dict[key] * quantity)))