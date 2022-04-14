from fractions import Fraction

def user_interface_data(data, title):
    print('{0} = {1}'.format(title, data))

def choose_operator():
    return str(input('С каким оператором будем работать?: '))

def choose_type_number():
    return str(input('С каким типом числа будем работать?: '))

def get_integer_value():
    return int(input('value = '))

def get_fraction_value():
    return Fraction(input('value = '))

def get_complex_value():
    return complex(input('value, без пробелов в виде "a+bj" = '))

def get_float_value():
    return float(input('value, через точку = '))




