import inspect
from timeit import default_timer as timer

from utils import register


def get_function_info(function):
    """

    :param function:
    :return:
    """
    def wrapper(*args, **kwargs):
        """
        :param args:
        :param kwargs:
        :return:
        """
        function_name = function.__name__
        count_function_call(function_name)
        execution_time, function_call = get_execution_time(args, kwargs)
        print(f"{function_name} call {register[function_name]} executed in {execution_time} seconds")
        function_info = format_function_info(args, function_call, function_name, kwargs)
        print(function_info)
        return function_call

    def format_function_info(args, function_call, function_name, kwargs):
        function_info = f'''
Name:  {function_name}
Type:   {type(function)}
Sign:   {inspect.signature(function)}
Args:   positional {args} 
        key-worded {kwargs}
        
Doc:    {function.__doc__}

Source: 
{"".join(inspect.getsourcelines(function)[0])}

Output: {function_call} '''
        return function_info

    def get_execution_time(args, kwargs):
        start = timer()
        function_call = function(*args, **kwargs)
        end = timer()
        execution_time = (end - start)
        return execution_time, function_call

    def count_function_call(function_name):
        if function_name in register.keys():
            register[function_name] = register[function_name] + 1
        else:
            register[function_name] = 1

    return wrapper
