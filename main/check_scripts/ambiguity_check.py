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


def is_vague(sentence):
    words = sentence.split(' ')
    for word in words:
        if word in vagueness:
            return True
    return False

def is_subjective(sentence):
    words = sentence.split(' ')
    for word in words:
        if word in subjectivity:
            return True
    return False

def is_optional(sentence):
    words = sentence.split(' ')
    for word in words:
        if word in optionality:
            return True
    return False

def is_implicit(sentence):
    words = sentence.split(' ')
    for word in words:
        if word in implicitness:
            return True
    return False


def check_ambiguity(sentences):
    res = []
    for sentence in sentences:
        vsoi = [0, 0, 0, 0]
        amb = 0
        if is_vague(sentence):
            vsoi[0] = 1
            amb = 1
        elif is_subjective(sentence):
            vsoi[1] = 1
            amb = 1
        elif is_optional(sentence):
            vsoi[2] = 1
            amb = 1
        elif is_implicit(sentence):
            vsoi[3] = 1
            amb = 1
        res.append([sentence, vsoi, amb])
    return res
