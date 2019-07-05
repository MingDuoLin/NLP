import random

human = """
human = 自己 寻找 活动
自己 = 我 | 俺 | 我们 
寻找 = 看看 | 找找 | 想找点
活动 = 乐子 | 玩的
"""

host = """
host = 寒暄 报数 询问 业务相关 结尾 
报数 = 我是 数字 号 ,
数字 = 单个数字 | 数字 单个数字 
单个数字 = 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 
寒暄 = 称谓 打招呼 | 打招呼
称谓 = 人称 ,
人称 = 先生 | 女士 | 小朋友
打招呼 = 你好 | 您好 
询问 = 请问你要 | 您需要
业务相关 = 玩玩 具体业务
玩玩 = 耍一耍 | 玩一玩
具体业务 = 喝酒 | 打牌 | 打猎 | 赌博
结尾 = 吗？"""


def create_grammar(gram_str, split='=', line_split='\n'):
    grammar = {}
    for lines in gram_str.split(line_split):
        if not lines.strip(): continue
        exp, stat = lines.split(split)
        grammar[exp.strip()] = [s.split() for s in stat.split('|')]
    return grammar


def generate(gram, target):
    if target not in gram: return target
    expand = [generate(gram, t) for t in random.choice(gram[target])]
    return ''.join(expand)


def generate_n(gram, target, num=10):
    return [generate(gram, target) for _ in range(num)]


def assign_1():
    print(generate_n(create_grammar(host), 'host'))


if __name__ == '__main__':
    assign_1()

