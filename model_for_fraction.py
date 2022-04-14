import user_interface as ui
from fractions import Fraction
import logger as log

x = 0
y = 0

def init(a, b):
    global x
    global y
    x = Fraction(a)
    y = Fraction(b)

def do_it(a, b):
    type_operator = ui.choose_operator()
    if type_operator == '+':
        result = a + b
        log.log_model_integer(result)
        return result
    if type_operator == '-':
        result = a - b
        log.log_model_integer(result)
        return result
    if type_operator == '*':
        result = a * b
        log.log_model_integer(result)
        return result
    if type_operator == '/':
        result = a / b
        log.log_model_integer(result)
        return result