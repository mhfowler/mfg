import spacy
import random
from image import gen_image
from mediachain import search
from yahoo import search as get_answer
from spacy.parts_of_speech import VERB, NOUN, ADJ

nlp = spacy.load('en')


def tell_fortune(question):
    doc = nlp(question)
    terms = [t.text for t in doc if t.pos in [VERB, NOUN, ADJ]]
    terms = random.sample(terms, min(3, len(terms)))
    while len(terms) < 3:
        terms.append(random.sample(terms, 1))

    img_urls = [random.choice(search(t)) for t in terms]

    text = get_answer(question)
    if text is None:
        text = get_answer(' '.join(terms))

    return gen_image(img_urls, question, text)


if __name__ == '__main__':
    import sys
    tell_fortune(sys.argv[1])