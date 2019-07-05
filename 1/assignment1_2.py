import re
import jieba
from collections import Counter
from assignment1_1 import host, create_grammar, generate_n


def cut(string): return list(jieba.cut(string))


def token(string): return re.findall('\w+', string)


def file_processing(file_name):
    with open(file_name, 'r+', encoding='UTF-8') as fp:
        file_str = [line.split('++$++')[2] for line in fp.readlines()]
    return [token(s)[0] for s in file_str]


def prob_2(word1, word2, words_count_2, TOKEN_2_GRAM):
    if word1 + word2 in words_count_2: return words_count_2[word1+word2] / len(TOKEN_2_GRAM)
    return 1 / len(TOKEN_2_GRAM)


def get_probability(sentence, words_count_2, TOKEN_2_GRAM):
    words = cut(sentence)
    sentence_pro = 1
    for i, word in enumerate(words[:-1]):
        next_ = words[i+1]
        sentence_pro *= prob_2(word, next_, words_count_2, TOKEN_2_GRAM)
    return sentence_pro


def generate_best(gram, target, words_count_2, TOKEN_2_GRAM):
    str_with_prob = [(g, get_probability(g, words_count_2, TOKEN_2_GRAM)) for g in generate_n(gram, target)]
    return sorted(str_with_prob, key = lambda x:x[1], reverse=True)[0]


def assign_2(words_count_2, TOKEN_2_GRAM):
    print(get_probability('小明今天抽奖抽到一架波音飞机', words_count_2, TOKEN_2_GRAM))
    print(get_probability('小明今天抽奖抽到一个苹果', words_count_2, TOKEN_2_GRAM))


def assign_3(words_count_2, TOKEN_2_GRAM):
    print(generate_best(create_grammar(host), 'host', words_count_2, TOKEN_2_GRAM))


if __name__ == '__main__':
    clean_str_list = file_processing('./train.txt')
    print(clean_str_list)
    TOKEN = []
    for i, line in enumerate(clean_str_list):
        # if i % 1000 == 0: print(i)
        TOKEN += cut(line)

    TOKEN_2_GRAM = [''.join(TOKEN[i:i + 2]) for i in range(len(TOKEN[:-1]))]
    words_count_2 = Counter(TOKEN_2_GRAM)
    print(words_count_2.most_common(10))

    assign_2(words_count_2, TOKEN_2_GRAM)
    assign_3(words_count_2, TOKEN_2_GRAM)

