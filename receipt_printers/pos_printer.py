import nltk
from hello_utilities.log_helper import _log
from hello_settings import PROJECT_PATH
import os

TEMP_PATH = os.path.join(PROJECT_PATH, 'temp')


def printer1(question):
    text = nltk.word_tokenize(question)
    pos_tags = nltk.pos_tag(text)
    # print pos_tags
    noun_tuples = filter(lambda x: x[1] in ['NN', 'JJ'], pos_tags)
    nouns = map(lambda x: x[0], noun_tuples)
    print nouns


if __name__ == '__main__':
    printer1('what banana is this?')
    f_path = os.path.join(PROJECT_PATH, 'receipt_printers/questions.txt')
    with open(f_path, 'r') as f:
        questions = f.read().split('\n')
        for question in questions:
            print question
            printer1(question)