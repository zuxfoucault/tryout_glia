import collections
def predict_beam(bigram=tuple(['i', 'would']), beam_size=4, sent_length=10, cnt2=cnt2, cnt3=cnt3):
    def loop_(bigram, cnt2, cnt3):
        dict_p = prob3.prob3(bigram, cnt2, cnt3)
        cand = collections.Counter(dict_p).most_common(beam_size)
        def loop_2(cand):
            for (w, v) in cand:
                bigram_[tuple([bigram[1], w])] = v
                dict_p2 = prob3.prob3(tuple([bigram[1], w]), cnt2, cnt3)
                cand_2 = collections.Counter(dict_p2).most_common(beam_size)
                for i in range(len(cand_2)):
                    result_dict[tuple([w, cand_2[i][0]])] = -cand_2[i][1] * v
                result = collections.Counter(result_dict).most_common(beam_size)
                result_dict1 = {}
                for i in range(len(result)):
                    result_dict1[result[i][0]] = result[i][1]
            return result_dict1
        result = loop_2(cand)
        return result

    def loop_3(result):
        result_2 = {}
        for (w, v) in result.items():
            dict_p = prob3.prob3(w[-2:], cnt2, cnt3)
            cand = collections.Counter(dict_p).most_common(beam_size)

            for (w_2, v_2) in cand:
                w1 = list(w)
                w1.append(w_2)
                result_2[tuple(w1)] = -v * v_2
        result_i = collections.Counter(result_2).most_common(beam_size)
        result_dict1 = {}
        for i in range(len(result_i)):
            result_dict1[result_i[i][0]] = result_i[i][1]
        return result_dict1

    count = 4
    result = loop_(bigram, cnt2, cnt3)
    while result and count <= 10:
        count += 1
        result = loop_3(result)
        tmp_key = []
        for i, j in result.items():
            if '.' in i:
                sentence_ = list(bigram)
                sentence_.extend(list(i))
                sentence.append(sentence_)
                tmp_key.append(i)

        for i in tmp_key:
            result.pop(i)

    for i, v in result.items():
        sentence_ = list(bigram)
        sentence_.extend(list(i[:8]))
        sentence.append(sentence_)

    return sentence

sentence = predict_beam(bigram=tuple(['i', 'would']), beam_size=4, sent_length=10, cnt2=cnt2, cnt3=cnt3)
print(sentence)
