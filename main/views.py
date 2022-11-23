from django.shortcuts import render, redirect
import json
import requests
from django.contrib import messages
from main.check_scripts.rule_check import check_structure
from main.check_scripts.ambiguity_check import check_ambiguity
from main.check_scripts.verifiability_check import check_verifiability
import re

def query(API_TOKEN, payload='', parameters=None, options={'use_cache': False}):
    API_URL = "https://api-inference.huggingface.co/models/EleutherAI/gpt-neo-2.7B"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    body = {"inputs":payload,'parameters':parameters,'options':options}
    response = requests.request("POST", API_URL, headers=headers, data= json.dumps(body))
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        return "Error:"+" ".join(response.json()['error'])
    else:
        return response.json()[0]['generated_text']

def recommend(prompt_q, request):
    API_TOKEN = "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"
    params = {
        'max_new_tokens': int(request.POST["token-length"]),  # number of generated tokens
        'temperature': float(request.POST["temperature"]),   # controlling the randomness of generations
        'end_sequence': request.POST["end-sequence"] # stopping sequence for generation
    }
    pre_prompts = "Football is played by gautam.\nActive: Gautam plays football.\n#\nFootball is played by him.\nActive: He plays football.\n#\nFootball is played by her.\nActive: She plays football.\n#\nFootball is played by them.\nActive: They play football.\n#\nFootball is played by us.\nActive: We play football.\n#\nFootball is played by me.\nActive: I play football.\n#\nFootball and Cricket are played by me.\nActive: I play football and cricket.\n#\nFootball was played by gautam.\nActive: Gautam played football.\n#\nFootball was played by him.\nActive: He played football.\n#\nFootball was played by her.\nActive: She played football.\n#\nFootball was played by them.\nActive: They played football.\n#\nFootball was played by us.\nActive: We played football.\n#\nFootball was played by me.\nActive: I played football.\n#\nFootball and Cricket were played by me.\nActive: I played football and cricket.\n#\nFootball will be played by gautam.\nActive: Gautam will play football.\n#\nFootball will be played by him.\nActive: He will play football.\n#\nFootball will be played by her.\nActive: She will play football.\n#\nFootball will be played by them.\nActive: They will play football.\n#\nFootball will be played by us.\nActive: We will play football.\n#\nFootball will be played by me.\nActive: I will play football.\n#\nFootball and Cricket will be played by me.\nActive: I will play football and cricket.\n#\nFootball is being played by gautam.\nActive: Gautam is playing football.\n#\nFootball is being played by him.\nActive: He is playing football.\n#\nFootball is being played by her.\nActive: She is playing football.\n#\nFootball is being played by them.\nActive: They are playing football.\n#\nFootball is being played by us.\nActive: We are playing football.\n#\nFootball is being played by me.\nActive: I am playing football.\n#\nFootball and Cricket are being played by me.\nActive: I am playing football and cricket.\n#\nFootball was being played by gautam.\nActive: Gautam was playing football.\n#\nFootball was being played by him.\nActive: He was playing football.\n#\nFootball was being played by her.\nActive: She was playing football.\n#\nFootball was being played by them.\nActive: They were playing football.\n#\nFootball was being played by us.\nActive: We were playing football.\n#\nFootball was being played by me.\nActive: I was playing football.\n#\nFootball and Cricket were being played by me.\nActive: I was playing football and cricket.\n#\nFootball has been played by gautam.\nActive: Gautam has played football.\n#\nFootball has been played by him.\nActive: He has played football.\n#\nFootball has been played by her.\nActive: She has played football.\n#\nFootball has been played by them.\nActive: They have played football.\n#\nFootball has been played by us.\nActive: We have played football.\n#\nFootball has been played by me.\nActive: I have played football.\n#\nFootball and Cricket have been played by me.\nActive: I have played football and cricket.\n#\nFootball had been played by gautam.\nActive: Gautam had played football.\n#\nFootball had been played by him.\nActive: He had played football.\n#\nFootball had been played by her.\nActive: She had played football.\n#\nFootball had been played by them.\nActive: They had played football.\n#\nFootball had been played by us.\nActive: We had played football.\n#\nFootball had been played by me.\nActive: I had played football.\n#\nFootball and Cricket had been played by me.\nActive: I had played football and cricket.\n#\nFootball will have been played by gautam.\nActive: Gautam will have played football.\n#\nFootball will have been played by him.\nActive: He will have played football.\n#\nFootball will have been played by her.\nActive: She will have played football.\n#\nFootball will have been played by them.\nActive: They will have played football.\n#\nFootball will have been played by us.\nActive: We will have played football.\n#\nFootball will have been played by me.\nActive: I will have played football.\n#\nFootball and Cricket will have been played by me.\nActive: I will have played football and cricket.\n#\nIs your task being done by you?\nActive: Are you doing your task?\n#\nWere those changes made by boss?\nActive: Did boss make those changes?\n#\nWhom did they invite to the party?\nActive: Who were invited to the party?\n#\nWho wrote this book?\nActive: By whom was this book written?\n#\nHad he been certified by the driving school?\nActive: Had the driving school certified him?\n#\nIs the candle lighted by you?\nActive: Do you light the candle?\n#\nIs a car being driven by me?\nActive: Am I driving a car?\n#\nHas my book been stolen by her?\nActive: Has she stolen my book?\n#\nWas work finished by him?\nActive: Did he finish work?\n#\nWere his books being revised by him?\nActive: Was he revising his books?\n#\nHad the assignment been completed by Sam?\nActive: Had Sam completed the assignment?\n#\nWill my tuition fee be paid by the university?\nActive: Will the university pay my tuition fee?\n#\nShall our home\nwork have been done by us?\nActive: Shall we have done our home\nwork?\n#\nBy whom are the students being taught?\nActive: Who is teaching the students?\n#\nCan the door be broken by him?\nActive: Can you break the door?\n#\nWhy is the ccar being washed by you?\nActive: Why are you washing the car?\n#\nHow is a cake made by you?\nActive: How do you make a cake?\n#\nBy which team was the match won?\nActive: Which team won the match?\n#\nWhat offer was put forth by him?\nActive: What offer did he put forth?\n#\nLet it be done at once.\nActive: Do it at once.\n#\nLet the wondows be opened.\nActive: Open the windows.\n#\nLearn your dialogues.\nActive: Let your dialogues be learnt."
    prompt = "\n#\n"+pre_prompts+prompt_q+"\nActive: "

    data = query(API_TOKEN, prompt, params)
    disp_output = data[len(pre_prompts)+len(prompt_q)+10:len(data)-2:1]

    print("\n\n===================================================================================")
    print(disp_output)
    print("===================================================================================\n\n")

    messages.info(request, 'Recommendation: '+disp_output)


def root(request):
    return redirect('index')


def index(request):
    return render(request, 'index.html')


def try_gpt(request):
    if request.method=="POST":        
        prompt_q = request.POST["prompt"]
        sentences = re.split(r'\. |\? |! |\.|\?|!', prompt_q)
        sentences = sentences[0:len(sentences)-1]
        
        struct_check_res = check_structure(sentences)
        for i in struct_check_res:
            print(i[1], i[0])
        
        amb_check_res = check_ambiguity(sentences)
        for i in amb_check_res:
            print(i[2], i[1], i[0])

        vrf_check_res = check_verifiability(sentences)
        for i in vrf_check_res:
            print(i[1], i[0])
        
        final_res = {}
        for i in range(len(struct_check_res)):
            final_res[struct_check_res[i][0]] = {
                    "struct": struct_check_res[i][1],
                    "vagueness": amb_check_res[i][1][0],
                    "subjectivity": amb_check_res[i][1][1],
                    "optionality": amb_check_res[i][1][2],
                    "implicitness": amb_check_res[i][1][3],
                    "ambiguity": amb_check_res[i][2],
                    "verifiability": vrf_check_res[i][1]
                    }

        params_to_front_end = {
            "final_res": final_res
        }
        
        return render(request, 'index.html', params_to_front_end)

    else:
        return render(request, 'index.html')