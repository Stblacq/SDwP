import inspect
from timeit import default_timer as timer

from Task3 import GetFunctionInfo, GetExecutionTimesAndCallCount
from utils import register, log


def get_execution_times_and_call_count_with_log(function):
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
        return function_call

    def get_execution_time(args, kwargs):
        start = timer()
        function_call = None
        try:
            function_call = function(*args, **kwargs)
        except Exception as error:
            log.error(f"{error}")
        end = timer()
        execution_time = (end - start)
        return execution_time, function_call

    def count_function_call(function_name):
        if function_name in register.keys():
            register[function_name] = register[function_name] + 1
        else:
            register[function_name] = 1

    return wrapper


def get_function_info_with_logging(function):
    def wrapper(*args, **kwargs):
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
        function_call = None
        try:
            function_call = function(*args, **kwargs)
        except Exception as error:
            log.error(f"{error}")
        end = timer()
        execution_time = (end - start)
        return execution_time, function_call

    def count_function_call(function_name):
        if function_name in register.keys():
            register[function_name] = register[function_name] + 1
        else:
            register[function_name] = 1

    return wrapper


class GetExecutionTimesAndCallCountWithLogging(GetExecutionTimesAndCallCount):
    def __call__(self, *args, **kwargs):
        try:
            function_call = super(GetExecutionTimesAndCallCountWithLogging, self).__call__(*args, **kwargs)
            return function_call
        except Exception as error:
            log.error(f"{error}")


class GetFunctionInfoWithLogging(GetFunctionInfo):
    def __call__(self, *args, **kwargs):
        try:
            function_call = super(GetFunctionInfoWithLogging, self).__call__(*args, **kwargs)
            return function_call
        except Exception as error:
            log.error(f"{error}")
