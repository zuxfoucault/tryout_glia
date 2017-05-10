from __future__ import division
import nltk
import re


def ngram_probs():
    bigram_p = {}
    bigram_pp = {}
    trigram_p = {}
    trigram_pp = {}
    unigram_p = {}

    filename = 'raw_sentences.txt'
    _WORD_FILTER = re.compile("([,!?\"':;)(])")
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

            for trigram in trigrams:
                if trigram not in trigram_p:
                   trigram_p[trigram] = 1
                else:
                   trigram_p[trigram] += 1
            sentence = source_f.readline()

        for trigram in trigram_p:
            trigram_pp[trigram] = trigram_p[trigram]/bigram_p[trigram[:2]]

        for bigram in bigram_p:
            bigram_pp[bigram] = bigram_p[bigram]/unigram_p[tuple([bigram[0]])]

    return bigram_pp, trigram_pp
