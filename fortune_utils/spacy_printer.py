# pip install spacy && python -m spacy.en.download
import spacy

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load('en')
# Process a document, of any size
text = open('war_and_peace.txt').read()
doc = nlp(text)

from spacy.attrs import *
# All strings mapped to integers, for easy export to numpy
np_array = doc.to_array([LOWER, POS, ENT_TYPE, IS_ALPHA])

from reddit_corpus import RedditComments
reddit = RedditComments('/path/to/reddit/corpus')
# Parse a stream of documents, with multi-threading (no GIL!)
# Processes over 100,000 tokens per second.
for doc in nlp.pipe(reddit.texts, batch_size=10000, n_threads=4):
    # Multi-word expressions, such as names, dates etc
    # can be merged into single tokens
    for ent in doc.ents:
        ent.merge(ent.root.tag_, ent.text, ent.ent_type_)
    # Efficient, lossless serialization --- all annotations
    # saved, same size as uncompressed text
    byte_string = doc.to_bytes()