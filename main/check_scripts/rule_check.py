#importing libraries 
from tabnanny import check
import nltk
import re
import spacy
from spacy.matcher import Matcher
from nltk.tokenize import sent_tokenize
nltk.download('punkt')
nlp=spacy.load('en_core_web_sm')

rule_1=['nsubj','iobj','dobj']
rule_2=['nsubj','dobj','mark','nsubj']
rule_3=['nsubj','mark','nsubj']
rule_4=['nsubj','neg','mark','xcomp','dobj']
rule_5=['nsubj','dobj','acl']
rule_6=['nsubj','dobj','acl']
rule_7=['nsubj','dobj','advmod']
rule_8=['nsubj','dobj','case','nmod']
rule_9=['nsubj','advmod','mark','xcomp']
rule_10=['nsubj','advmod','nsubj','advcl']
rule_11=['nsubj','mark','xcomp']
rule_12=['nsubj','xcomp']
rule_13=['nsubj','advmod']
rule_14=['nsubj','attr']
rule_15=['nsubj','case','nummod','nmod']
rule_16=['nsubjpass','auxpass','case','nmod']
rule_17=['nsubj','dobj']
rule_18=['nsubj'] 
rule_19=['nsubj','case','nmod']
rule_20=['mark'] 
rule_21=['nsubj','dobj','neg','mark','acl']
rule_22=['nsubj','dobj','mark','attr','xcomp']
rule_23=['nsubj','dobj','mark','acl']
rule_24=['nsubj','nsubj','xcomp']
rule_25=['nsubj','dobj','advmod','mark','xcomp']
rule_26=['advmod','mark'] 
rule_27=['nsubjpass','aux','auxpass','ROOT','case','nmod']
rule_28=['nsubj','ROOT','dobj']
rule_29=['nsubj','ROOT','dobj','pobj']
rule_30=['nsubj','ROOT','pobj']
rule_31=['nsubj','ROOT','dobj','dobj']


def printer(line,t,rule):
  ans=""
  i=0
  j=0
  while(t[i]!=rule[j]):
    i=i+1
  if(i==len(t)-1):
    print("false")
  else:
    ans+=line[i]
    j=j+1
    while(i<len(t) and j<len(rule)):
      if(t[i]==rule[j]):
        j=j+1
      if(j!=len(rule)):
        i=i+1
        ans+=" "
        ans+=line[i]
  if(j==len(rule)):
    return ans
  else:
    ans=""
    return ans

def is_passive(sentence):
    doc = nlp(sentence)
    matcher = Matcher(nlp.vocab)
    passive_rule = [{'DEP': 'nsubjpass'}, {'DEP': 'aux', 'OP': '*'}, {'DEP': 'auxpass'}, {'TAG': 'VBN'}]
    matcher.add('Passive', [passive_rule])
    matches = matcher(doc)
    if matches:
        return True
    else:
        return False

def sentence_partition(inp,td,tag):
    st=inp[td.index(tag):td.index('cc')]
    st1=inp[td.index(tag):td.index('cc')-1]
    end=inp[td.index('cc')+1:]
    temp=" ".join(st)
    temp+="."
    temp+=" ".join(st1)
    temp+=" "
    temp+=" ".join(end)
    temp+="."
    return temp

def conjuction_checker(inp):
    return any(['cc' in inp])

def matcher(rule,inp):
    i=0
    j=0
    while i<len(rule) and j<len(inp):
        if(rule[i]==inp[j]):
            i=i+1
            j=j+1
        else:
            j=j+1
    return i==len(rule)

def matcher2(rule,inp,pos_list,pos_tag):
    flag=False
    if pos_tag in pos_list:
        flag=True
    i=0
    j=0
    while i<len(rule) and j<len(inp):
        if(rule[i]==inp[j]):
            i=i+1
            j=j+1
        else:
            j=j+1
    return (flag and i==len(rule))

def detect_rules(sentence):
    cleaned_sentence = re.sub('\s+', ' ', sentence.lower())

    TDs_text=[]
    temp=nlp(cleaned_sentence)
    t=[]
    for i in temp:
        t.append([i.text,i.pos_ ,i.dep_ ])
    TDs_text.append(t)
    
    ans=[]
    ans_string=""
    for sentence in TDs_text:
        pos_list=[]
        tag_list=[]
        line=[]
        sentence_string=""
        tag_string=""
        ans_string=""
        for word in sentence:
            line.append(word[0])
            sentence_string+=word[0]
            sentence_string+=" " 
            tag_string+=word[2]
            tag_string+=" , "   
            pos_list.append(word[1])
            tag_list.append(word[2])
    
        if(is_passive(sentence_string)):
            ans_string+=sentence_string
            ans_string+="."
            ans.append([sentence_string,tag_string,'passive voice',"The sentence is in passive voice,Change into Active voice"])

        elif(matcher(rule_4,tag_list)):
            temp=printer(line,tag_list,rule_4)
            ans_string+=temp
            ans_string+="."
            if(conjuction_checker(tag_list)):
                ans_string=sentence_partition(line,tag_list,'nsubj')
            ans.append([sentence_string,tag_string,'SSR 4',ans_string])

        elif(matcher(rule_22,tag_list)):
            temp=printer(line,tag_list,rule_22)
            ans_string+=temp
            ans_string+="."
            if(conjuction_checker(tag_list)):
                ans_string=sentence_partition(line,tag_list,'nsubj')
            ans.append([sentence_string,tag_string,'SSR 22',ans_string])

        elif(matcher(rule_21,tag_list)):
            temp=printer(line,tag_list,rule_21)
            ans_string+=temp
            ans_string+="."
            if(conjuction_checker(tag_list)):
                ans_string=sentence_partition(line,tag_list,'nsubj')
            ans.append([sentence_string,tag_string,'SSR 21',ans_string])

        elif(matcher(rule_25,tag_list)):
            temp=printer(line,tag_list,rule_25)
            ans_string+=temp
            ans_string+="."
            if(conjuction_checker(tag_list)):
                ans_string=sentence_partition(line,tag_list,'nsubj')
            ans.append([sentence_string,tag_string,'SSR 25',ans_string])

        elif(matcher(rule_2,tag_list)):
            temp=printer(line,tag_list,rule_2)
            ans_string+=temp
            ans_string+="."
            if(conjuction_checker(tag_list)):
                ans_string=sentence_partition(line,tag_list,'nsubj')
            ans.append([sentence_string,tag_string,'SSR 2',ans_string])

        elif(matcher(rule_8,tag_list)):
            temp=printer(line,tag_list,rule_8)
            ans_string+=temp
            ans_string+="."
            if(conjuction_checker(tag_list)):
                ans_string=sentence_partition(line,tag_list,'nsubj')
            ans.append([sentence_string,tag_string,'SSR 8',ans_string])

        elif(matcher(rule_9,tag_list)):
            temp=printer(line,tag_list,rule_9)
            ans_string+=temp
            ans_string+="."
            if(conjuction_checker(tag_list)):
                ans_string=sentence_partition(line,tag_list,'nsubj')
            ans.append([sentence_string,tag_string,'SSR 9',ans_string])

        elif(matcher(rule_10,tag_list)):
            temp=printer(line,tag_list,rule_10)
            ans_string+=temp
            ans_string+="."
            if(conjuction_checker(tag_list)):
                ans_string=sentence_partition(line,tag_list,'nsubj')
            ans.append([sentence_string,tag_string,'SSR 10',ans_string])

        elif(matcher(rule_15,tag_list)):
            temp=printer(line,tag_list,rule_15)
            ans_string+=temp
            ans_string+="."
            if(conjuction_checker(tag_list)):
                ans_string=sentence_partition(line,tag_list,'nsubj')
            ans.append([sentence_string,tag_string,'SSR 15',ans_string])

        elif(matcher(rule_23,tag_list)):
            temp=printer(line,tag_list,rule_23)
            ans_string+=temp
            ans_string+="."
            if(conjuction_checker(tag_list)):
                ans_string=sentence_partition(line,tag_list,'nsubj')
            ans.append([sentence_string,tag_string,'SSR 23',ans_string])

        elif(matcher(rule_19,tag_list)):
            temp=printer(line,tag_list,rule_19)
            ans_string+=temp
            ans_string+="."
            if(conjuction_checker(tag_list)):
                ans_string=sentence_partition(line,tag_list,'nsubj')
            ans.append([sentence_string,tag_string,'SSR 19',ans_string])

        elif(matcher(rule_29,tag_list)):
            temp=printer(line,tag_list,rule_29)
            ans_string+=temp
            ans_string+="."
            if(conjuction_checker(tag_list)):
                ans_string=sentence_partition(line,tag_list,'nsubj')
            ans.append([sentence_string,tag_string,'SSR 29',ans_string])

        elif(matcher(rule_31,tag_list)):
            temp=printer(line,tag_list,rule_31)
            ans_string+=temp
            ans_string+="."
            if(conjuction_checker(tag_list)):
                ans_string=sentence_partition(line,tag_list,'nsubj')
            ans.append([sentence_string,tag_string,'SSR 30',ans_string])

        elif(matcher(rule_1,tag_list)):
            temp=printer(line,tag_list,rule_1)
            ans_string+=temp
            ans_string+="."
            if(conjuction_checker(tag_list)):
                ans_string=sentence_partition(line,tag_list,'nsubj')
            ans.append([sentence_string,tag_string,'SSR 1',ans_string])

        elif(matcher(rule_3,tag_list)):
            temp=printer(line,tag_list,rule_3)
            ans_string+=temp
            ans_string+="."
            if(conjuction_checker(tag_list)):
                ans_string=sentence_partition(line,tag_list,'nsubj')
            ans.append([sentence_string,tag_string,'SSR 3',ans_string])

        elif(matcher2(rule_5,tag_list,pos_list,'VBG')):
            temp=printer(line,tag_list,rule_5)
            ans_string+=temp
            ans_string+="."
            if(conjuction_checker(tag_list)):
                ans_string=sentence_partition(line,tag_list,'nsubj')
            ans.append([sentence_string,tag_string,'SSR 5',ans_string])

        elif(matcher2(rule_6,tag_list,pos_list,'VBN')):
            temp=printer(line,tag_list,rule_6)
            ans_string+=temp
            ans_string+="."
            if(conjuction_checker(tag_list)):
                ans_string=sentence_partition(line,tag_list,'nsubj')
            ans.append([sentence_string,tag_string,'SSR 6',ans_string])

        elif(matcher(rule_7,tag_list)):
            temp=printer(line,tag_list,rule_7)
            ans_string+=temp
            ans_string+="."
            if(conjuction_checker(tag_list)):
                ans_string=sentence_partition(line,tag_list,'nsubj')
            ans.append([sentence_string,tag_string,'SSR 7',ans_string])

        elif(matcher(rule_11,tag_list)):
            temp=printer(line,tag_list,rule_11)
            ans_string+=temp
            ans_string+="."
            if(conjuction_checker(tag_list)):
                ans_string=sentence_partition(line,tag_list,'nsubj')
            ans.append([sentence_string,tag_string,'SSR 11',ans_string])

        elif(matcher(rule_19,tag_list)):
            temp=printer(line,tag_list,rule_19)
            ans_string+=temp
            ans_string+="."
            if(conjuction_checker(tag_list)):
                ans_string=sentence_partition(line,tag_list,'nsubj')
            ans.append([sentence_string,tag_string,'SSR 19',ans_string])

        elif(matcher2(rule_24,tag_list,pos_list,'JJ')):
            temp=printer(line,tag_list,rule_24)
            ans_string+=temp
            ans_string+="."
            if(conjuction_checker(tag_list)):
                ans_string=sentence_partition(line,tag_list,'nsubj')
            ans.append([sentence_string,tag_string,'SSR 24',ans_string])

        elif(matcher(rule_28,tag_list)):
            temp=printer(line,tag_list,rule_28)
            ans_string+=temp
            ans_string+="."
            if(conjuction_checker(tag_list)):
                ans_string=sentence_partition(line,tag_list,'nsubj')
            ans.append([sentence_string,tag_string,'SSR 28',ans_string])

        elif(matcher(rule_30,tag_list)):
            temp=printer(line,tag_list,rule_30)
            ans_string+=temp
            ans_string+="."
            if(conjuction_checker(tag_list)):
                ans_string=sentence_partition(line,tag_list,'nsubj')
            ans.append([sentence_string,tag_string,'SSR 30',ans_string])

        elif(matcher(rule_12,tag_list)):
            temp=printer(line,tag_list,rule_12)
            ans_string+=temp
            ans_string+="."
            if(conjuction_checker(tag_list)):
                ans_string=sentence_partition(line,tag_list,'nsubj')
            ans.append([sentence_string,tag_string,'SSR 12',ans_string])

        elif(matcher(rule_14,tag_list)):
            temp=printer(line,tag_list,rule_14)
            ans_string+=temp
            ans_string+="."
            if(conjuction_checker(tag_list)):
                ans_string=sentence_partition(line,tag_list,'nsubj')
            ans.append([sentence_string,tag_string,'SSR 14',ans_string])

        elif(matcher(rule_17,tag_list)):
            temp=printer(line,tag_list,rule_17)
            ans_string+=temp
            ans_string+="."
            if(conjuction_checker(tag_list)):
                ans_string=sentence_partition(line,tag_list,'nsubj')
            ans.append([sentence_string,tag_string,'SSR 17',ans_string])

        elif(matcher(rule_26,tag_list)):
            temp=printer(line,tag_list,rule_16)
            ans_string+=temp
            ans_string+="."
            if(conjuction_checker(tag_list)):
                ans_string=sentence_partition(line,tag_list,'nsubjpass')
            ans.append([sentence_string,tag_string,'SSR 26',ans_string])

        elif(matcher(rule_13,tag_list)):
            temp=printer(line,tag_list,rule_13)
            ans_string+=temp
            ans_string+="."
            if(conjuction_checker(tag_list)):
                ans_string=sentence_partition(line,tag_list,'nsubj')
            ans.append([sentence_string,tag_string,'SSR 13',ans_string])

        elif(matcher(rule_18,tag_list)):
            temp=printer(line,tag_list,rule_18)
            ans_string+=temp
            ans_string+="."
            if(conjuction_checker(tag_list)):
                ans_string=sentence_partition(line,tag_list,'nsubj')
            ans.append([sentence_string,tag_string,'SSR 18',ans_string])

        elif(matcher(rule_20,tag_list)):
            temp=printer(line,tag_list,rule_20)
            ans_string+=temp
            ans_string+="."
            if(conjuction_checker(tag_list)):
                ans_string=sentence_partition(line,tag_list,'mark')
            ans.append([sentence_string,tag_string,'SSR 20',ans_string])

        else:
            ans_string+=sentence_string
            ans_string+="."
            ans.append([sentence_string,tag_string,'NA','NA'])
    
    return ans


def check_structure(sentences):
    res = []
    for sentence in sentences:
        judgement = detect_rules(sentence)
        print(judgement)
        if(judgement[0][2]=='passive voice'):
            res.append([sentence, 0])
        else:
            res.append([sentence, 1])
    return res
