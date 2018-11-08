# Import the some function
from modA.modB.my_file import a_sum_function

sum_res = a_sum_function(3 + 4)
print(f'Sum {sum_res}')


# Import the constant
from modA.modB.my_file import A_CONSTANT

print(f'The constant value is {A_CONSTANT}')


# Import the class
from modA.modB.my_file import ACarClass

car = ACarClass('red', 125)
print(car.describe())
