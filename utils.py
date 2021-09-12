import logging
import os
import sys

register = {}

logging.basicConfig(format="[%(asctime)s] %(levelname)s %(message)s - %(pathname)s",
                    filename=os.path.join("error.log"))
log = logging.getLogger('error.log')


def enable_print():
    sys.stdout = sys.__stdout__


def block_print():
    sys.stdout = open(os.devnull, 'w')


def peak_print(value):
    enable_print()
    print(value)
    block_print()
