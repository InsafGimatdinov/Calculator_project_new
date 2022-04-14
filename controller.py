import model_for_integer as modint
import model_for_fraction as modfr
import model_for_complex as modcom
import model_for_float as modfl
import user_interface as ui

def botton_click():
    type_number = ui.choose_type_number()
    if type_number == 'integer':
        value_a = ui.get_integer_value()
        value_b = ui.get_integer_value()
        modint.init(value_a, value_b)
        result = modint.do_it(value_a, value_b)
    elif type_number == 'fraction':
        value_a = ui.get_fraction_value()
        value_b = ui.get_fraction_value()
        modfr.init(value_a, value_b)
        result = modfr.do_it(value_a, value_b)
    elif type_number == 'complex':
        value_a = ui.get_complex_value()
        value_b = ui.get_complex_value()
        modcom.init(value_a, value_b)
        result = modcom.do_it(value_a, value_b)
    elif type_number == 'float':
        value_a = ui.get_float_value()
        value_b = ui.get_float_value()
        modfl.init(value_a, value_b)
        result = modfl.do_it(value_a, value_b)
    else:
        return 'Такого типа нет'
    ui.user_interface_data(result, 'result')



