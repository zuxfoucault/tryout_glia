import nltk
import re
from __future__ import division
bigram_p = {}
trigram_p = {}
unigram_p = {}

filename = 'raw_sentences.txt'
_WORD_FILTER = re.compile("([.,!?\"':;)(])")


def ngram_probs(filename):
with open(filename, mode="r") as source_f:
    sentence = source_f.readline()
    while sentence:
        sentence = _WORD_FILTER.sub('', sentence)  # Punctuation
        sentence = sentence.lower()  # lower case
        tokens = sentence.split()
        unigrams = (tuple(nltk.ngrams(tokens, 1)))
        bigrams = (tuple(nltk.ngrams(tokens, 2)))
        trigrams = (tuple(nltk.ngrams(tokens, 3)))
        for unigram in unigrams:
            if unigram not in unigram_p:
                unigram_p[unigram] = 1
            else:
                unigram_p[unigram] += 1

        for bigram in bigrams:
            if bigram not in bigram_p:
               bigram_p[bigram] = 1
            else:
               bigram_p[bigram] += 1

            for bigram in bigram_p:
                bigram_p[bigram] = bigram_p[bigram]/unigram_p[bigram[0]

        for trigram in trigrams:
            if trigram not in trigram_p:
               trigram_p[trigram] = 1
            else:
               trigram_p[trigram] += 1

            for trigram in trigram_p:
                trigram_p[bigram] = trigram_p[bigram]/bigram_p[bigram[0]
        sentence = source_f.readline()

    return bigram_p, trigram_p
