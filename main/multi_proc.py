import os
import multiprocessing
from collections import OrderedDict
from main.check_scripts.rule_check import check_passive
from main.check_scripts.ambiguity_check import check_ambiguity
from main.check_scripts.verifiability_check import check_verifiability

# # Execution logic: Method for lemmatization, ambiguity check, verifiability check, passive-voice check, and recommendations.
def analyze(sentences, chunk_num, return_val_dict):
    final_res = {}
    detected = {
        'Vague': [],
        'Subjective': [],
        'Optional': [],
        'Implicit': [],
        'Non-Verifiable': [],
        'Passive': []
    }
    recommended = {}
    
    for sentence in sentences:
        amb_check_res = check_ambiguity(sentence)
        vrf_check_res = check_verifiability(sentence)
        passive_check_res = check_passive(sentence)
        
        vagueness, subjectivity, optionality, impliciteness, ambiguity, verifiability, voice, rec, verdict  = '-', '-', '-', '-', 'NO', 'YES', 'Active', '-', 1
        if amb_check_res[1][0][0]==True:
            vagueness = amb_check_res[1][0][1]
            for word in vagueness: detected['Vague'].append(word)
        if amb_check_res[1][1][0]==True:
            subjectivity = amb_check_res[1][1][1]
            for word in subjectivity: detected['Subjective'].append(word)
        if amb_check_res[1][2][0]==True:
            optionality = amb_check_res[1][2][1]
            for word in optionality: detected['Optional'].append(word)
        if amb_check_res[1][3][0]==True:
            impliciteness = amb_check_res[1][3][1]
            for word in impliciteness: detected['Implicit'].append(word)
        if amb_check_res[0]==True:
            ambiguity = 'YES'
        if vrf_check_res[0]==False:
            verifiability = 'NO due to ' + str(vrf_check_res[1])
            for word in vrf_check_res[1]: detected['Non-Verifiable'].append(word)
        if passive_check_res==True:
            voice = 'Passive'
            # rec = recommend(sentence)
            rec = '-----Recommendation engine not in use----'
            recommended[sentence] = rec
        
        if ambiguity!='NO' or verifiability!='YES' or voice=='Passive':
            verdict = 0
        final_res[sentence] = {
            "vagueness": vagueness,
            "subjectivity": subjectivity,
            "optionality": optionality,
            "implicitness": impliciteness,
            "ambiguity": ambiguity,
            "verifiability": verifiability,
            "passive": voice,
            "rec": rec,
            "verdict": verdict
        }

        for key, value in detected.items():
            value = set(value)
        detected['Rec'] = recommended
    
    print(f"[Checkpoint-3.3.{chunk_num}]: MultiProcessing: Requirement Analysis completed for data chunk [{chunk_num}]")
    return_val_dict[chunk_num] = (final_res, detected)


def run_multi_proc(sliced_input):
    proc_manager = multiprocessing.Manager()
    return_val_dict = proc_manager.dict()
    proc_list = []
    
    # chunk_files = [f for f in os.listdir('data_chunks') if os.path.isfile(os.path.join('data_chunks', f))]
    chunk_num = 1
    
    print(f"[Checkpoint---3.1]: MultiProcessing: Beginning parallel processing for {len(sliced_input)} data chunks.")
    for sentences_in_this_chunk in sliced_input:
        # f = open('data_chunks\\'+cf, 'r')
        # chunk_content = f.read()
        # sentences = chunk_content.split("|||")
        proc = multiprocessing.Process(target=analyze, args=(sentences_in_this_chunk, chunk_num, return_val_dict))
        proc_list.append(proc)
        proc.start()
        print(f"[Checkpoint-3.2.{chunk_num}]: MultiProcessing: Execution triggered for sub-process [{chunk_num}]. Analyzing data chunk.")
        chunk_num += 1
    
    for proc in proc_list:
        proc.join()
    print("[Checkpoint---3.4]: MultiProcessing: All sub-processes executed successfully.")

    sorted_return_val_dict = OrderedDict(sorted(return_val_dict.items()))
    
    final_res_split = [res for res, found in sorted_return_val_dict.values()]
    final_res = {}
    for res in final_res_split:
        final_res.update(res)
    
    detected_split = [found for res, found in sorted_return_val_dict.values()]
    detected = {}
    for found in detected_split:
        detected.update(found)
    
    return final_res, detected