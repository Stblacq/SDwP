import random
import time

from Task1 import get_execution_times_and_call_count
from Task2 import get_function_info
from Task3 import GetFunctionInfo, GetExecutionTimesAndCallCount
from Task4 import get_execution_times_and_call_count_with_log, get_function_info_with_logging, \
    GetExecutionTimesAndCallCountWithLogging, GetFunctionInfoWithLogging


@get_execution_times_and_call_count
def function_1():
    print("I am ready to Start")
    result = 0
    n = random.randint(10, 751)
    for i in range(n):
        result += (i ** 2)


@get_execution_times_and_call_count
def function_2(n=2, m=5):
    print("I am ready to do serious stuff")
    max_val = float('-inf')
    n = random.randint(n, 751)
    res = [pow(i, m) for i in range(n)]
    for i in res:
        if i > max_val:
            max_val = i


@get_function_info
def function_3(principal, rate, tenor=10):
    """
    This function calculates simple interest
    :param tenor: duration of investment
    :param principal: The amount to invest
    :param rate: The annual rate
    :returns simple_interest
    """
    return principal * rate * tenor


@GetExecutionTimesAndCallCount
def function_4(principal, rate, tenor=10):
    """
    This function calculates simple interest
    :param tenor: duration of investment
    :param principal: The amount to invest
    :param rate: The annual rate
    :returns simple_interest
    """
    return principal * rate * tenor


@GetFunctionInfo
def function_5(principal, rate, tenor=10):
    """
    This function calculates simple interest
    :param tenor: duration of investment
    :param principal: The amount to invest
    :param rate: The annual rate
    :returns simple_interest
    """
    return principal * rate * tenor


@get_execution_times_and_call_count_with_log
def function_6(n=2, m=5):
    print("I am ready to do serious stuff")
    max_val = float('-inf')
    n = random.randint(n, 751)
    res = [pow(i, m) for i in range(n)]
    for i in res:
        if i > max_val:
            max_val = i


@get_function_info_with_logging
def function_7(principal, rate, tenor=10):
    """
    This function calculates simple interest
    :param tenor: duration of investment
    :param principal: The amount to invest
    :param rate: The annual rate
    :returns simple_interest
    """
    return principal * rate * tenor


@GetExecutionTimesAndCallCountWithLogging
def function_8(principal, rate, tenor=10):
    """
    This function calculates simple interest
    :param tenor: duration of investment
    :param principal: The amount to invest
    :param rate: The annual rate
    :returns simple_interest
    """
    return principal * rate * tenor


@GetFunctionInfoWithLogging
def function_9(principal, rate, tenor=10):
    """
    This function calculates simple interest
    :param tenor: duration of investment
    :param principal: The amount to invest
    :param rate: The annual rate
    :returns simple_interest
    """
    return principal * rate * tenor


def bench_mark_function(n=3):
    time.sleep(n)
    print(f"I slept for {n} seconds, now I'm awake")
