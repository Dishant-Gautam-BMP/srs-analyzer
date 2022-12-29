from django.shortcuts import render, redirect
import json
import requests
import re
import xlsxwriter
import fitz
import os
from datetime import datetime
from django.contrib import messages
from main.check_scripts.rule_check import check_passive
from main.check_scripts.ambiguity_check import check_ambiguity
from main.check_scripts.verifiability_check import check_verifiability
from main.models import file_upload
# from main.ambiguity import *
# from main.verifiability import *




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


def recommend(sentence):
    API_TOKEN = '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'
    params = {
        'max_new_tokens': 100,  # number of generated tokens
        'temperature': 0.11,    # controlling the randomness of generations
        'end_sequence': '###'   # stopping sequence for generation
    }

    pre_prompt = 'A customer may cancel a transaction at any time; the transaction is terminated and the card is ejected. Active: A customer may cancel a transaction at any time; the system terminates the transaction and the card is ejected.\n###\nAfter the successful validation of the pin/atm card, the user is given a selection of performing a withdrawal, query, or transfer. Active: After the successful validation of the pin/atm card, the system gives the user a selection of performing a withdrawal, query, or transfer.\n###\nBefore a withdrawal transaction can be approved, the system determines that sufficient funds exist in the chosen account; the maximum daily will not exceed; and that there are sufficient funds at the local cash dispenser. Active: Before the system can approve a withdrawal transaction, the system determines that sufficient funds exist in the chosen account; the maximum daily will not exceed; and that there are sufficient funds at the local cash dispenser.\n###\nComplete cmo_information usecase is carried out. Active: The system carries out complete cmo_information usecase.\n###\nCustomer selects to use the credit card which is stored in the system. Active: Customer selects to use the credit card which the system stores.\n###\nFor this, the system redirects to create family profile page and createfamilyprofile usecase is carried out. Active: For this, the system redirects to create family profile page and the system carries out the createfamilyprofile usecase.\n###\nThe books should be stored in database. Active: The system must store the books in database.\n###\nThe marvel electronic store product web page should be loaded. Active: The system should load the marvel electronic store product web page.\n###\nMembers should be stored in the database. Active: The system should store members in the database.\n###\nIf admin selects to remove bus, then removebus usecase is carried out. Active: If admin selects to remove bus, then the system carries out the removebus usecase.\n###\nIf all mandatory fields are not completed then consumer is asked to complete them to proceed. Active: If all mandatory fields are not completed then the system asks the consumer to complete them to proceed.\n###\nIf customer is stuck in the process then he can use help facility to know how to fill the information, helpfacility usecase is carried out. Active: If customer is stuck in the process then he can use help facility to know how to fill the information, the system carries out the helpfacility usecase.\n###\nIf in the deletion process registrar decides not to delete the professor, then the delete operation is cancelled. Active: If in the deletion process registrar decides not to delete the professor, then the system cancels the delete operation.\n###\nIf it is in progress, then a message is displayed to the registrar that the registration is in progress because the close registration processing can not be performed if registration is in progress. Active: If it is in progress, then the system desplays a message to the registrar that the registration is in progress because the system cannot perform the close registration processing if registration is in progress.\n###\nIf no book is selected by the user then the system again asks user to select a book to reserve. Active: If the user selects no book then the system again asks user to select a book to reserve.\n###\nIf no category is selected by the user then the system again asks user to select a category. Active: If the user selects no category then the system again asks user to select a category.\n###\nIf no information is shown then the system asks caregiver to refresh the page. Active: If the system shows no information then the system asks caregiver to refresh the page.\n###\nIf no subject is chosen by the student then the system asks student to select a subject again. Active: If the student chooses no subject then the system asks student to select a subject again.\n###\nIf the consumer is not logged in with"create individual profile" then an error message is occurred. Active: If the consumer is not logged in with"create individual profile" then the system occurs an error message.\n###\nIf the customer is not sure about how to proceed then he uses help facility, helpfacility usecase is carried out. Active: If the customer is not sure about how to proceed then he uses help facility, the system carries out the helpfacility usecase.\n###\nIf the pin is validated satisfactorily, the customer is prompted to choose a withdrawal, query, or transfer transaction. Active: If the pin is validated satisfactorily, the system prompts the customer to choose a withdrawal, query, or transfer transaction.\n###\nIf the schedule contains “ enrolled in ” course offerings, then the student is removed from the course offering. Active: If the schedule contains “ enrolled in ” course offerings, then the system removes the student from the course offering.\n###\nIf the system can not find any grade information from the previous semester for the student then a message is displayed. Active: If the system can not find any grade information from the previous semester for the student then the system displays a message.\n###\nIf the transaction is approved, the requested amount of cash is dispended, a receipt is printed containing information about the transaction, and the card is ejected. Active: If the transaction is approved, the system dispenses the requested amount of cash, prints a receipt containing information about the transaction, and ejects the card.\n###\nIf the user presses the up-button, an up-elevator is requested. Active: If the user presses the up-button, the system requests an up-elevator.\n###\nShe is instructed to enter her uid and password in a secure web page and to create her individual profile. Active: The system instructs her to enter her uid and password in a secure web page and to create her individual profile.\n###\nSystem displays login page, log-in usecase is carried out. Active: System displays login page, the system carries out log-in usecase.\n###\nThe billing system is notified for each student in each course offering that is not cancelled, so the student can be billed for the course offering. Active: The system notifies the billing system for each student in each course offering that is not cancelled, so the student can be billed for the course offering.\n###\nThe card is ejected. Active: The system ejects the card.\n###\nThe customer can use help facility, helpfacility usecase is carried out. Active: The customer can use help facility, the system carries out helpfacility usecase.\n###\nThe help service can be invoked independently by the customer, which will provide him with a “ main ” help page. Active: The customer can independently invoke the help service, which will provide him with a “ main ” help page.\n###\nThe student can also update or delete course selections if changes are made within the add/drop period at the beginning of the semester. Active: The student can also update or delete course selections if they make changes within the add/drop period at the beginning of the semester.\n###\nThe supplier needs to log in, log-in usecase is carried out. Active: The supplier needs to log in, the system carries out log-in usecase.\n###\nThe system confirms that the items are reserved to be delivered. Active: The system confirms that the system reserves items to be delivered.\n###\nThe system validates that the doors of the elevator are closed after the request is processed. Active: The system validates that the doors of the elevator are closed after the system processes the request.\n###\nThe users are validated by the system. Active: The system validates the users.\n###\nThen specifyservices usecase is carried out. Active: Then the system carries out specifyservices usecase.\n###\nWhenever user presses a button, that button gets illuminated. Active: Whenever user presses a button, the system illuminates that button.\n###\n'
    prompt = pre_prompt+sentence+' Active:'

    data = query(API_TOKEN, prompt, params)
    rec_out = data[len(pre_prompt)+len(sentence)+9:len(data)-4:1]

    # print("\n===================================================================================")
    # print(data)
    # print("===================================================================================\n")

    return rec_out


def analyze(sentences):
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
            rec = recommend(sentence)
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
    return final_res, detected


def generate_excel(res):
    wb_name = 'generated_workbooks/'+datetime.now().strftime("%Y-%m-%d_%H-%M-%S")+'.xlsx'
    wb = xlsxwriter.Workbook(wb_name)
    ws = wb.add_worksheet()

    header_cell_format = wb.add_format({'bold': True})
    correct_cell_format = wb.add_format({'bg_color': '#99FF99'})
    incorrect_cell_format = wb.add_format({'bg_color': '#FF9999'})
    ws.write(0, 0, 'Sentence', header_cell_format)
    ws.write(0, 1, 'Vagueness', header_cell_format)
    ws.write(0, 2, 'Subjectivity', header_cell_format)
    ws.write(0, 3, 'Optionality', header_cell_format)
    ws.write(0, 4, 'Implicitness', header_cell_format)
    ws.write(0, 5, 'Ambiguity', header_cell_format)
    ws.write(0, 6, 'Verifiability', header_cell_format)
    ws.write(0, 7, 'Voice', header_cell_format)
    ws.write(0, 8, 'Recommendation', header_cell_format)
    i = 1
    for key, val in res.items():
        if val['verdict']==1:
            ws.write(i, 0, key, correct_cell_format)
        else:
            ws.write(i, 0, key, incorrect_cell_format)
        j = 1
        for k, v in val.items():
            if j==9:
                break
            if val['verdict']==1:
                ws.write(i, j, str(v), correct_cell_format)
            else:
                ws.write(i, j, str(v), incorrect_cell_format)
            j = j+1
        i = i+1
    wb.close()
    return wb_name


def find_latest_pdf():
    files_list = os.listdir('media')
    paths = [os.path.join('media', basename) for basename in files_list]
    try:
        return max(paths, key=os.path.getctime)
    except:
        return None
    return None


def read_pdf():
    latest_file = find_latest_pdf()
    srs = fitz.open(latest_file)
    srs_content = ""
    for page in srs:
        srs_content += page.get_text()
    return srs_content


def annotate_pdf(detected):
    print(detected)
    print('Annotating PDF.......')
    latest_file = find_latest_pdf()
    srs = fitz.open(latest_file)
    for pg, page in enumerate(srs):
        for key, value in detected.items():
            if key=='Rec':
                for sentence, rec in value.items():
                    matched_values = page.search_for(sentence)
                    # print(matched_values)
                    for item in matched_values:
                        annot = page.add_underline_annot(item)
                        annot.set_colors({"stroke":(1,0,0)})
                        info = annot.info
                        info["title"]   = 'Passive Voice'
                        info["content"] = 'Active-voice Recommendation: '+rec
                        annot.set_info(info)
                        annot.update()
            else:
                for item in value:
                    matched_values = page.search_for(' '+item+' ')
                    matched_values + page.search_for(' '+item+'.')
                    matched_values + page.search_for(' '+item+',')
                    matched_values + page.search_for(' '+item+'?')
                    matched_values + page.search_for(' '+item+'!')
                    # print(matched_values)
                    for item in matched_values:
                        annot = page.add_rect_annot(item)
                        annot.set_border({"dashes":[],"width":1})
                        if key=='Vague':
                            annot.set_colors({"stroke":(0,0,1)})
                        elif key=='Subjective':
                            annot.set_colors({"stroke":(0.6,0.3,0)})
                        elif key=='Optional':
                            annot.set_colors({"stroke":(1,0,1)})
                        elif key=='Implicit':
                            annot.set_colors({"stroke":(1,0.6,0)})
                        elif key=='Non-Verifiable':
                            annot.set_colors({"stroke":(0.6,0,1)})
                        info = annot.info
                        info["title"]   = key
                        info["content"] = 'This word makes the sentence '+key.lower()+'.'
                        annot.set_info(info)
                        annot.update()
    annotated_pdf = latest_file[0:len(latest_file)-4]+'_annotated.pdf'
    srs.save(annotated_pdf, garbage=3, deflate=True)
    srs.close()
    print('Completed annotating PDF.......')
    return annotated_pdf




def root(request):
    return redirect('index')


def index(request):
    return render(request, 'index.html')


def analyze_reqs(request):
    if request.method=="POST":
        text_content, pdf_content, content = '', None, ''
        text_content = request.POST["prompt"]
        try:
            file = request.FILES["file"]
        except:
            file = None
        
        if file==None:
            print(text_content)
            if text_content!='':
                content = text_content
            else:
                messages.info(request, 'No input detected!')
                return render(request, 'index.html')

        if file is not None:
            doc = file_upload.objects.create(file=file)
            doc.save()
            pdf_content = read_pdf()
            if pdf_content is None:
                messages.info(request, 'Unsupported file format or empty file!')
                return render(request, 'index.html')
            content = pdf_content
        else:
            content = text_content


        sentences = re.split(r'\. |\? |! |\.|\?|!', content)
        sentences = sentences[0:len(sentences)-1]
        final_res, detected = analyze(sentences)
        excel_url = generate_excel(final_res)
        annotated_pdf_url = ''
        if pdf_content!='': annotated_pdf_url = annotate_pdf(detected)

        params_to_front_end = {
            "final_res": final_res,
            "excel_url": excel_url,
            "annotated_pdf_url": annotated_pdf_url
        }
        return render(request, 'output.html', params_to_front_end)

    else:
        return render(request, 'output.html')