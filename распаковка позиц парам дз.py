def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


values_list = [ 1, '2', True]
values_dict = { 'a': 1, 'b': '5', "c": False}
values_list_2 = [1, '6']




print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)
