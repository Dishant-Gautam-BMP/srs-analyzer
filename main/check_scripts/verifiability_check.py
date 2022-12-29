import re
from nltk.stem import WordNetLemmatizer


unquantifiable_words = [
    'able',
    'ably',
    'about',
    'abundance',
    'abundantly',
    'acceptable',
    'accessible',
    'achievable',
    'active',
    'adaptable',
    'adept',
    'adequacy',
    'adequate',
    'adjustable',
    'admirable',
    'adroit',
    'advantageous',
    'adventitious',
    'agreeable',
    'almost',
    'alterable',
    'always',
    'ample',
    'ampleness',
    'amply',
    'apparently',
    'approximate',
    'around',
    'assumably',
    'available',
    'avoidably',
    'basic',
    'believably',
    'benefic',
    'beneficial',
    'benignant',
    'big',
    'blameless',
    'blanket',
    'boundless',
    'broad',
    'calmy',
    'capable',
    'capacious',
    'carefully',
    'cautiously',
    'changeable',
    'charitable',
    'chiefly',
    'cinch',
    'circa',
    'classy',
    'clear',
    'clever',
    'close',
    'cometence',
    'comformble',
    'comfortable',
    'commendable',
    'commending',
    'commensurate',
    'common',
    'comparative',
    'competent',
    'compliant',
    'comprising',
    'conceivable',
    'conformable',
    'congruous',
    'considerable',
    'considerate',
    'consistently',
    'constantly',
    'convenient',
    'conventional',
    'convertible',
    'coolly',
    'credible',
    'customary',
    'decent',
    'decisive',
    'deft',
    'deluxe',
    'dependable',
    'desirable',
    'dexterous',
    'dormant',
    'ductile',
    'dynamic',
    'easy',
    'easygoing',
    'economic',
    'effective',
    'effectual',
    'efficient',
    'effortless',
    'elementary',
    'energetic',
    'enough',
    'equal',
    'estimable',
    'eternally',
    'evenly',
    'ever',
    'everlastingly',
    'evermore',
    'everydayextensive',
    'evident',
    'excellent',
    'exceptional',
    'exemplary',
    'expandable',
    'expansible',
    'expected',
    'expendiently',
    'expert',
    'extendable',
    'extended',
    'extendible',
    'extensible',
    'extensile',
    'extensive',
    'facile',
    'fair',
    'familiar',
    'familier',
    'favorable',
    'favoring',
    'favourable',
    'favouring',
    'feasible',
    'first-class',
    'fitted',
    'flawless',
    'flexible',
    'fluently',
    'forevermore',
    'fortuitous',
    'freely',
    'fresh',
    'fruitful',
    'general',
    'generic',
    'genuine',
    'gettable',
    'gnarly',
    'good',
    'gratifying',
    'great',
    'guiltless',
    'habitual',
    'handily',
    'handy',
    'harmlessly',
    'healthy',
    'hefty',
    'helpful',
    'honorable',
    'honourable',
    'huge',
    'humdrum',
    'ideal',
    'imaginable',
    'immeasurable',
    'imminent',
    'impending',
    'impervious',
    'impregnable',
    'inclusive',
    'incorrupt',
    'inculpable',
    'indeterminate',
    'interest',
    'invariably',
    'irreprehensible',
    'irreproachable',
    'justified',
    'large',
    'latent',
    'lengthy',
    'light',
    'little',
    'long',
    'looming',
    'loosely',
    'loyal',
    'lucrative',
    'maintained',
    'major',
    'malleable',
    'manifest',
    'marvelous',
    'masterly',
    'maybe',
    'mere',
    'meritious',
    'modifiable',
    'moldable',
    'most',
    'much',
    'natural',
    'near',
    'nearabout',
    'neat',
    'nice',
    'normal',
    'nothing',
    'obedient',
    'objectionable',
    'obtainable',
    'obvious',
    'optional',
    'orderly',
    'ordinarity',
    'ordinary',
    'organized',
    'orthodox',
    'overall',
    'painless',
    'paltry',
    'passable',
    'perchance',
    'perfect',
    'perhaps',
    'pervasive',
    'platic',
    'plausibly',
    'pleasing',
    'plenitude',
    'pliable',
    'pliant',
    'popular',
    'positive',
    'possible',
    'potent',
    'potential',
    'pplain',
    'practicable',
    'practical',
    'practically',
    'praiseworthy',
    'precious',
    'prepetually',
    'prerogative',
    'presumably',
    'presumptively',
    'primarily',
    'prime',
    'probable',
    'proficient',
    'promising',
    'propitious',
    'prosperous',
    'protractible',
    'protractile',
    'public',
    'pure',
    'pushover',
    'qualified',
    'quality',
    'quickly',
    'readily',
    'realizable',
    'reasonably',
    'rectitude',
    'regular',
    'relative',
    'reliable',
    'repeatedly',
    'reputable',
    'requisite',
    'resilient',
    'respectable',
    'righteous',
    'righteousness',
    'roomy',
    'rough',
    'roundly',
    'routine',
    'safe',
    'salubrious',
    'satisfactory',
    'scopic',
    'secured',
    'seemingly',
    'several',
    'shrewd',
    'simple',
    'sizable',
    'skilled',
    'skillfully',
    'smooth',
    'snap',
    'some',
    'sound',
    'spacious',
    'splendid',
    'stretchable',
    'strightforward',
    'stupendous',
    'sufficiency',
    'sufficient',
    'sufficing',
    'suitable',
    'super',
    'superb',
    'supple',
    'surely',
    'sweeping',
    'thinkable',
    'thorough',
    'tolerable',
    'tractable',
    'treasure',
    'trustworthy',
    'typical',
    'unblemished',
    'unceasingly',
    'uncertain',
    'uncomplicated',
    'uncontaminated',
    'uncorrupted',
    'undamaged',
    'unessentially',
    'unexceptional',
    'unimpaired',
    'universal',
    'unobjectionable',
    'unrestricted',
    'unspoiled',
    'useful',
    'usual',
    'valuable',
    'variable',
    'vast',
    'viable',
    'vigorous',
    'virtually',
    'virtue',
    'well',
    'whatever',
    'wholesome',
    'wide',
    'widley',
    'wonderful',
    'workable',
    'worth',
    'worthwhile'
]

unquantifiable_phrases = [
    'a bit',
    'a little',
    'all around',
    'all encompassing',
    'all in all',
    'all right',
    'almost always',
    'as arule',
    'as good as',
    'can do',
    'close to',
    'easily done',
    'en masse',
    'familiar with',
    'for keeps',
    'good at',
    'hand over fist',
    'hands down',
    'hanging loose',
    'in effect',
    'in essence',
    'in general',
    'in perpetuum',
    'in substance',
    'in the region of',
    'in the vicinity of',
    'just about',
    'just like that',
    'like nothing',
    'more or less',
    'no problem',
    'no sweat',
    'no trouble',
    'not far from',
    'not limited to',
    'not quite',
    'on average',
    'on the whole',
    'part of',
    'pretty near',
    'till blue in the face',
    'till cows come here',
    'till hell freezes over',
    'to be',
    'upwards of',
    'very close',
    'well organized',
    'with ease',
    'within a little',
    'within reach',
    'without excepton'
]




lemmatizer = WordNetLemmatizer()

def check_verifiability(sentence):
    words = sentence.split(' ')
    lemmatized_words = []
    for word in words:
        lemmatized_words.append(lemmatizer.lemmatize(word))
    res = [True, []]
    for i in range(len(words)):
        if words[i] in unquantifiable_words or lemmatized_words[i] in unquantifiable_words:
            res[1].append(words[i])
    for phrase in unquantifiable_phrases:
        if re.search(' '+phrase+' ', sentence) or re.search('^'+phrase, sentence) or re.search(phrase+'$', sentence):
            res[1].append(phrase)
    if len(res[1])>0:
        res[0] = False
    return res

# ress = check_verifiability("This must work efficiently")
# print(ress)