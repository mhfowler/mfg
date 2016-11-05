import nltk
from hello_utilities.log_helper import _log
from hello_settings import PROJECT_PATH
import os
import random

import mediachain

TEMP_PATH = os.path.join(PROJECT_PATH, 'temp')


def get_keywords(question):
    text = nltk.word_tokenize(question)
    pos_tags = nltk.pos_tag(text)
    keyword_tuples = filter(lambda x: x[1] in ['NN', 'JJ'], pos_tags)
    keywords = map(lambda x: x[0], keyword_tuples)
    return keywords


def printer1(question):
    keywords = get_keywords(question)
    for k in keywords:
        imgs = mediachain.search(k)
        if imgs:
            _log(random.choice(imgs))


if __name__ == '__main__':
    printer1('what banana is this?')
    f_path = os.path.join(PROJECT_PATH, 'receipt_printers/questions.txt')
    with open(f_path, 'r') as f:
        questions = f.read().split('\n')
        samples = random.sample(questions, 5)
        for question in samples:
            _log('**********************')
            _log('**********************')
            _log('**********************')
            _log('**********************')
            _log(question)
            printer1(question)