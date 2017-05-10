import w_c
import math


cnt2, cnt3 = w_c.ngram_probs()
bigram = tuple(['place', 'like'])

def prob3(bigram, cnt2, cnt3):
    dict_p = {}
    for (a, b, c), v in cnt3.items():
        if a == bigram[0] and b == bigram[1]:
            dict_p[c] = math.log(float(v))
    return dict_p
