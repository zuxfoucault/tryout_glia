import w_c
import prob3

bigram = tuple(['i', 'would'])


def predict_max(bigram, sent_length=15):
    sentence = [i for i in bigram]
    cnt2, cnt3 = w_c.ngram_probs()
    w = str()
    while len(sentence) <= sent_length and w != '.':
        dict_p = prob3.prob3(bigram, cnt2, cnt3)
        w = max(dict_p, key=lambda i: dict_p[i])
        sentence.append(w)
        bigram = tuple([bigram[1], w])
    return sentence
