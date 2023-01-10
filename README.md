# Software Requirements Analyzer

## Abstract
<p align="justify">
A software requirements document helps the software developer(s) understand the needs they are to cater to while building a software product. It gives a detailed overview of the software product, clearly mentioning the parameters it should abide by. Proper understanding and documentation of the goals of the product are required to reduce the cost, time, and effort of redesigning the product. This human-drafted document, written in natural language, requires validation before it can serve as a blueprint for the actual development of the software. Our Software Requirements Analyzer, examines such requirements documents, points out flaws, and gives correct recommendations to the user. It uses a novel model, combining natural language processing, list-based determination, rule-based classification, and transformers. This tool finds the ambiguity and non-verifiability present in requirements documents and recommends the user active-voice versions of sentences in passive voice.
</p><br>

## User guide
Carry out the following steps to use the Software Requirements Analyzer on your machine:
1. Clone this repository.
2. Create a new virtual environment using the Python command: ```py -m venv <name-of-your-virtual-env>```
3. Install all the packages mentioned in the ```requirements.txt``` file using the command: ```pip install -r requirements.txt```
4. Navigate to the root directory of this repository.
5. Execute ```py manage.py runserver``` to run the web application on your local server.
6. Analyze software requirements seamlessly!
