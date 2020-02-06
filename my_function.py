import numpy as np

function_name = None
min_val = 0
max_val = 0


def init(name):
    global function_name, min_val, max_val
    function_name = name
    if function_name == 'rastrigin':
        min_val = -6
        max_val = 6
    elif function_name == 'ackley':
        min_val = -15
        max_val = 15
    elif function_name == 'sphere':
        min_val = -15
        max_val = 15
    elif function_name == 'rosenbrock':
        min_val = -2.5
        max_val = 2.5
    elif function_name == 'easom':
        min_val = -100
        max_val = 100
    elif function_name == 'griewank':
        min_val = -100 # -600
        max_val = 100 # 600
    elif function_name == 'styblinski':
        min_val = -5
        max_val = 5


def my_function(x, y):
    if function_name == 'rastrigin':
        return 20 + x ** 2 - 10 * np.cos(2 * np.pi * x) + y ** 2 - 10 * np.cos(2 * np.pi * y)  # rastrigin [-6, 6]
    elif function_name == 'sphere':
        return x ** 2 + y ** 2  # sferna funkcija
    elif function_name == 'rosenbrock':
        return 100 * (x ** 2 - y) ** 2 + (x - 1) ** 2  # rozenbrokova funkcija [-2.5, 2.5]
    elif function_name == 'griewank':
        return 1 + (x ** 2 + y ** 2) / 4000 - (np.cos(x) * np.cos(y / np.sqrt(2)))  # grivankova [-600, 600]
    elif function_name == 'ackley':
        return 20 + np.e - 20 * np.exp(-0.2 * np.sqrt((x ** 2 + y ** 2) / 2)) - np.exp(
            -(np.cos(2 * np.pi * x) + np.cos(2 * np.pi * y)) / 2)  # aklijeva [-15, 15]
    elif function_name == 'easom':
        return - np.cos(x) * np.cos(y) * np.exp(- ((x - np.pi) ** 2 + (y - np.pi) ** 2))  # easom function [-100, 100]
    elif function_name == 'styblinski':
        return (x ** 4 - 16 * x ** 2 + 5 * x + y ** 4 - 16 * y ** 2 + 5 * y) / 2  # styblinski [-5,5]


def analytic_result():
    if function_name == 'rastrigin':
        return [0, 0], 0
    elif function_name == 'ackley':
        return [0, 0], 0
    elif function_name == 'sphere':
        return [0, 0], 0
    elif function_name == 'rosenbrock':
        return [1, 1], 0
    elif function_name == 'easom':
        return [3.1415, 3.1415], -1
    elif function_name == 'styblinski':
        return [-2.903534, -2.903534], -78.332
    elif function_name == 'griewank':
        return [0, 0], 0

