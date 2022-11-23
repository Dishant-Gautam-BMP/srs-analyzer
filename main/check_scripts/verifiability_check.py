import re

unquantifiable = [
    'good',
    'well',
    'adequate',
    'efficient',
    'enough',
    'sufficient',
    'approximately',
    'nearly always',
    'generally',
    'typically',
    'several',
    'to be defined',
    'not limited to',
    'possibly',
    'probably',
    'optionally',
    'adaptable',
    'extensible',
    'easy',
    'familiar',
    'safe'
]


def check_verifiability(sentences):
    res = []
    for sentence in sentences:
        vrf = 1
        words = sentence.split(' ')
        for word in words:
            if word in unquantifiable:
                vrf = 0
                break
        res.append([sentence, vrf])
    return res
