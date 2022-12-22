import re

vagueness = [
    'may',
    'could',
    'has to',
    'have to',
    'might',
    'will',
    'should have',
    'must have',
    'all the other',
    'all other',
    'based on',
    'some',
    'appropriate',
    'as a',
    'as an',
    'a minimum',
    'up to',
    'adequate',
    'as applicable',
    'be able to',
    'be capable',
    'but not limited to',
    'capability of',
    'capability to',
    'effective',
    'normal',
    'a few',
    'a lot of',
    'about',
    'any',
    'approximate',
    'approximately',
    'as a maximum',
    'as a minimum',
    'as appropriate',
    'as much as possible',
    'as far as possible',
    'as little as possible',
    'as required',
    'as necessary',
    'at least',
    'as possible',
    'be capable of',
    'best possible',
    'possibly',
    'eventually',
    'if possible',
    'if needed',
    'if case',
    'similarly',
    'take into account',
    'take into consideration',
    'clear,easy,easily',
    'strong',
    'good',
    'bad',
    'efficient',
    'useful',
    'suitable',
    'significant',
    'fast',
    'recent',
    'far',
    'close',
    'in front',
    'can',
    'worse',
    'having in mind',
    'probably',
    'clearly',
    'slow',
    'near'
]

subjectivity = [
    'similar',
    'better',
    'similarly',
    'worse',
    'having in mind',
    'take into account',
    'take into consideration',
    'as possible'
]

optionality = [
    'can',
    'may',
    'optionally',
    'possibly',
    'eventually',
    'if in case',
    'if possible',
    'if appropriate',
    'if needed'
]

implicitness = [
    'this',
    'these',
    'that',
    'those',
    'it',
    'they',
    'previous',
    'next',
    'following',
    'last',
    'above',
    'below'
]

# imperatives = ['shall', 'must', 'is required to', 'are applicable', 'are to', 'responsible for', 'will', 'should', 'could', 'would']
# conjunctions : ['and', 'after', 'although', 'as long as', 'before', 'but', 'else', 'if', 'in order', 'in case', 'nor', 'or', 'otherwise', 'once', 'since', 'then', 'though', 'till', 'unless', 'until', 'when', 'whenever', 'where', 'whereas', 'wherever', 'while', 'yet']




def is_vague(words):
    res = [False, []]
    for word in words:
        if word in vagueness:
            res[1].append(word)
    if len(res[1])>0:
        res[0] = True
    return res

def is_subjective(words):
    res = [False, []]
    for word in words:
        if word in subjectivity:
            res[1].append(word)
    if len(res[1])>0:
        res[0] = True
    return res

def is_optional(words):
    res = [False, []]
    for word in words:
        if word in optionality:
            res[1].append(word)
    if len(res[1])>0:
        res[0] = True
    return res

def is_implicit(words):
    res = [False, []]
    for word in words:
        if word in implicitness:
            res[1].append(word)
    if len(res[1])>0:
        res[0] = True
    return res


def check_ambiguity(sentence):
    words = sentence.split(' ')
    vsoi = [[], [], [], []]
    vsoi[0] = is_vague(words)
    vsoi[1] = is_subjective(words)
    vsoi[2] = is_optional(words)
    vsoi[3] = is_implicit(words)
    if vsoi[0]==[False, []] and vsoi[1]==[False, []] and vsoi[2]==[False, []] and vsoi[3]==[False, []]:
        return [False, vsoi]
    return [True, vsoi]

# ress = check_ambiguity("The software can be heavy or light.")
# print(ress)