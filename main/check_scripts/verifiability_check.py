import re

unquantifiable = [
    'good',
    'adequate',
    'adequatly',
    'efficient',
    'efficiently',
    'enough',
    'sufficient',
    'sufficiently',
    'approximate',
    'approximately',
    'near',
    'nearly',
    'always',
    'general',
    'generally',
    'typical',
    'typically',
    'several',
    'to be defined',
    'not limited to',
    'possibly',
    'probably',
    'optionally',
    'adaptable',
    'extensive',
    'extensible',
    'easily',
    'easy',
    'familiarly',
    'familiar',
    'safe',
    'safely'
]


def check_verifiability(sentence):
    words = sentence.split(' ')
    res = [True, []]
    for word in words:
        if word in unquantifiable:
            res[1].append(word)
    if len(res[1])>0:
        res[0] = False
    return res

# ress = check_verifiability("This must work efficiently")
# print(ress)