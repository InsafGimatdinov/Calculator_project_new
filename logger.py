from datetime import datetime as dt
import model_for_integer as modint
import model_for_fraction as modfr
import model_for_complex as modcom
import model_for_float as modfl

def log_model_integer(result):
    time = dt.now().strftime('%M:%S')
    first_value = modint.x
    second_value = modint.y
    with open('log_calc.csv', 'a') as file:
        file.write('{}; first_value = {}; second_value = {}; result = {}\n'
                   .format(time, first_value, second_value, result))

def log_model_fraction(result):
    time = dt.now().strftime('%M:%S')
    first_value = modfr.x
    second_value = modfr.y
    with open('log_calc.csv', 'a') as file:
        file.write('{}; first_value = {}; second_value = {}; result = {}\n'
                   .format(time, first_value, second_value, result))

def log_model_complex(result):
    time = dt.now().strftime('%M:%S')
    first_value = modcom.x
    second_value = modcom.y
    with open('log_calc.csv', 'a') as file:
        file.write('{}; first_value = {}; second_value = {}; result = {}\n'
                   .format(time, first_value, second_value, result))

def log_model_float(result):
    time = dt.now().strftime('%M:%S')
    first_value = modfl.x
    second_value = modfl.y
    with open('log_calc.csv', 'a') as file:
        file.write('{}; first_value = {}; second_value = {}; result = {}\n'
                   .format(time, first_value, second_value, result))
