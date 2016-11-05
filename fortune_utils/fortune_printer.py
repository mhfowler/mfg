from hello_utilities.log_helper import _log
from google import google, images
from hello_settings import PROJECT_PATH
import os
import random


proverb_path = os.path.join(PROJECT_PATH, 'receipt_printers/proverbs.txt')


def printer1(question):
    print question
    with open(proverb_path, 'r') as f:
        lines = f.read().split('\n')
        proverb = random.choice(lines)
        print proverb


if __name__ == '__main__':
    printer1('what banana is this?')