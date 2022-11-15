import re

unquantifiable = [
    'good',
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


def check_verifiability(content):
    res = []
    sentences = re.split(r'\. |\? |! |\.|\?|!', content)
    sentences = sentences[0:len(sentences)-1]
    for sentence in sentences:
        ver = 1
        words = sentence.split(' ')
        for word in words:
            if word in unquantifiable:
                ver = 0
                break
        res.append([sentence, ver])
    return res

# ress = check_verifiability("Hello! How are you? Yeah, I'm good! I hope the same for you.")
# print(ress)