import random


def is_variable(pat):
    """
    判断pat是否为Variable: ？X
    """
    return pat.startswith('?') and all(s.isalpha() for s in pat[1:])


def pat_match(pattern, saying):
    """
    判断saying是否符合pattern,并返回pattern变量
    """
    if is_variable(pattern[0]):
        return pattern[0], saying[0]
    else:
        if pattern[0] != saying[0]:
            return False
        else:
            return pat_match(pattern[1:], saying[1:])


def pat_match_(pattern, saying):
    """
    判断saying是否符合pattern,并支持返回多个pattern变量
    """
    if not pattern or not saying: return []

    if is_variable(pattern[0]):
        return [(pattern[0], saying[0])] + pat_match_(pattern[1:], saying[1:])
    else:
        if pattern[0] != saying[0]:
            return []
        else:
            return pat_match_(pattern[1:], saying[1:])


def pat_to_dict(patterns):
    """
    将解析结果保存在dictionary
    """
    return {k:v for k,v in patterns}


def substitute(rule, parsed_rules):
    """
    替换模板中?X为解析结果
    """
    if not rule: return []

    return [parsed_rules.get(rule[0], rule[0])] + substitute(rule[1:], parsed_rules)


defined_patterns = {
    "I need ?X": ["Image you will get ?X soon", "Why do you need ?X ?"],
    "My ?X told me something": ["Talk about more about your ?X", "How do you think about your ?X ?"]
}


def get_response(saying, rules):
    """" please implement the code, to get the response as followings:

    >>> get_response('I need iPhone')
    >>> Image you will get iPhone soon
    >>> get_response("My mother told me something")
    >>> Talk about more about your monther.
    """
    got_patterns = pat_match_(rules.split(), saying.split())
    if got_patterns:
        pat_dict = pat_to_dict(got_patterns)
        return ' '.join(substitute(random.choice(defined_patterns[rules]).split(), pat_dict))
    else:
        return False


def test():
    assert pat_match('I want ?X'.split(), "I want holiday".split()) == ('?X', 'holiday')
    assert pat_match('I have dreamed a ?X'.split(), "I dreamed about dog".split()) == False
    assert pat_match('I dreamed about ?X'.split(), "I dreamed about dog".split())== ('?X', 'dog')
    assert pat_match_("?X greater than ?Y".split(), "3 greater than 2".split()) == [('?X', '3'), ('?Y', '2')]
    assert pat_match_("I want ?X".split(), "I want iPhone".split()) == [('?X', 'iPhone')]
    assert substitute("What if you mean if you got a ?X".split(), pat_to_dict([('?X', 'iPhone')])) == ['What', 'if', 'you', 'mean', 'if', 'you', 'got', 'a', 'iPhone']

    print(get_response('I need iPhone', 'I need ?X'))


if __name__ == '__main__':
    test()

