from timeit import default_timer as timer

from utils import register


def get_execution_times_and_call_count(function):
    def wrapper(*args, **kwargs):
        function_name = function.__name__
        count_function_call(function_name)
        execution_time, function_call = get_execution_time(args, kwargs)
        print(f"{function_name} call {register[function_name]} executed in {execution_time} seconds")
        return function_call

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
