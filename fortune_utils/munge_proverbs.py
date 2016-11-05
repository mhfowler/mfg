import nltk
from hello_utilities.log_helper import _log
from hello_settings import PROJECT_PATH
import os
import random
import re


from HTMLParser import HTMLParser


class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()




if __name__ == '__main__':
    f_path = os.path.join(PROJECT_PATH, 'receipt_printers/proverbs_raw.txt')
    with open(f_path, 'r') as f:
        lines = f.read().split('\n')
        proverbs = []
        for line in lines:
            if line.startswith('####'):
                line = line.replace('####', '')
                line = strip_tags(line)
                proverbs.append(line)
        o_path = os.path.join(PROJECT_PATH, 'receipt_printers/proverbs.txt')
        with open(o_path, 'w') as out_file:
            for proverb in proverbs:
                out_file.write(proverb + '\n')
