from gensim.models import KeyedVectors
from nltk.corpus import movie_reviews
import random
import numpy
w2v = KeyedVectors.load_word2vec_format("wiki.en.5k.vec", binary=False)
#print("Number of words: %d" % len(w2v.vocab))

def we_represent(tokens):
    vec = numpy.zeros(300)
    for tok in tokens:
        if tok.lower() in w2v:
            vec += w2v[tok]
    return vec

training_instances = []
training_labels = []
test_instances = []
test_labels = []

for label in movie_reviews.categories():
    for fileid in movie_reviews.fileids(label):
        doc = movie_reviews.words(fileid)
        instance = we_represent(doc)
        if label == 'pos':
            lbl = 1
        else:
            lbl = 0
        if random.randint(0, 9) == 0:
            test_instances.append(instance)
            test_labels.append(lbl)
        else:
            training_instances.append(instance)
            training_labels.append(lbl)

print(training_instances)
print(training_labels)
print(test_instances)
print(test_labels)