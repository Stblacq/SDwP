import inspect
import time
from timeit import default_timer as timer

from Task1 import get_execution_times_and_call_count
from Task2 import get_function_info
import pandas as pd

from utils import block_print, peak_print, enable_print, register


class GetExecutionTimesAndCallCount:
    def __init__(self, function):
        self.function = function
        self.function_name = self.function.__name__

    def __call__(self, *args, **kwargs):
        self.count_function_call(self.function_name)
        execution_time, function_call = self.get_execution_time(args, kwargs)
        with open('output.txt', 'a') as f:
            print(f"{self.function_name} call {register[self.function_name]}"
                  f" executed in {execution_time} seconds", file=f)
        return function_call

    @staticmethod
    def count_function_call(function_name):
        if function_name in register.keys():
            register[function_name] = register[function_name] + 1
        else:
            register[function_name] = 1

    def get_execution_time(self, args, kwargs):
        start = timer()
        function_call = self.function(*args, **kwargs)
        end = timer()
        execution_time = (end - start)
        return execution_time, function_call


class GetFunctionInfo(GetExecutionTimesAndCallCount):

    def __call__(self, *args, **kwargs):
        function_call = super(GetFunctionInfo, self).__call__(*args, **kwargs)
        function_info = self.format_function_info(args, function_call, self.function_name, kwargs)
        with open('output.txt', 'a') as f:
            print(function_info, file=f)
        return function_call

    def format_function_info(self, args, function_call, function_name, kwargs):
        function_info = f'''
    Name:  {function_name}
    Type:   {type(self.function)}
    Sign:   {inspect.signature(self.function)}
    Args:   positional {args} 
            key-worded {kwargs}

    Doc:    {self.function.__doc__}

    Source: 
{"".join(inspect.getsourcelines(self.function)[0])}

    Output: {function_call} '''
        return function_info


decorators = [get_execution_times_and_call_count, get_function_info, GetExecutionTimesAndCallCount, GetFunctionInfo]


def rank_decorators(test_function, *args, **kwargs):
    """

    :param test_function: Function to use as benchmark
    :param args: function argument
    :param kwargs: function keyword
    :return: rank_table dataframe
    """
    block_print()  # Disable Printing From Nested Functions
    rank_table = {}
    for index, decorator in enumerate(decorators):
        decorator_name = decorator.__name__
        peak_print(f" {index + 1}/{len(decorators)} Testing {decorator_name}") # Show Progress
        decorated_test_function = decorator(test_function)
        execution_time = get_execution_time(args, kwargs, decorated_test_function)
        rank_table[decorator_name] = execution_time
    rank_table = sorted(rank_table.items(), key=lambda kv: kv[1])
    data = {'PROGRAM': [x[0] for x in rank_table],
            'RANK': [x + 1 for x in range(len(rank_table))],
            'TIME ELAPSED': [x[1] for x in rank_table]}
    rank_dataframe = pd.DataFrame.from_dict(data)
    enable_print() # Re enable print
    print(rank_dataframe) #Show Rank table
    return rank_dataframe


def get_execution_time(args, kwargs, test_function):
    start = timer()
    test_function(*args, **kwargs)
    end = timer()
    execution_time = (end - start)
    return execution_time
