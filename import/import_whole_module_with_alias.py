# Import the whole 'my_file' module

import modA.modB.my_file as my_file

sum_res = my_file.a_sum_function(3 + 4)
print(f'Sum {sum_res}')

print(f'The constant value is {my_file.A_CONSTANT}')

car = my_file.ACarClass('red', 125)
print(car.describe())
