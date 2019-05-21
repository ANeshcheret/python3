# def decorator(func_to_decorate):
#     def wrapper():
#         print('Before function runs')
#         func_to_decorate()
#         print('After function runs')
#     return wrapper
#
# @decorator
# def print_string():
#     print("I'm print_string() functions")
#
# print_string()

# def decorator_passing_args(func_to_decorate):
#     def wrapper_with_arg(arg1, arg2):
#         print('I have args:', arg1, arg2)
#         func_to_decorate(arg1, arg2)
#     return wrapper_with_arg
#
# @decorator_passing_args
# def print_fullname(first_name, last_name):
#     print("My name is:", first_name, last_name)
#
# print_fullname('Andrey', 'Neshcheret')

def method_decorator(method_to_decorate):
    def wrapper(self, lie):
        lie = lie - 3
        return  method_to_decorate(self, lie)
    return wrapper

class Lisa():
    def __init__(self):
        self.age = 35

    @method_decorator
    def sayyourage(self, lie):
        print("I'm {}, what do you think?".format(self.age + lie))

lisa = Lisa()
lisa.sayyourage(0)
