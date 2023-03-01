# Abstract_Reader

The purpose of this project is to speed up a bibliographic review of literature. By passing the abstract of each paper 
from a list of papers and instructing an OpenAI text-completion/instruct model to 'Determine whether this abstract from 
the paper /TITLE/ describes or includes /THIS TOPIC/, you must start with the word 'yes' or 'no' in your answer.' The 
last sentence in our prompt enables the collection of model responses to be parsed for either word to classify whether 
a paper does or does not describe or include the user's intended topic. 

# Example Output

C:\Users\********\PycharmProjects\Abstract_Reader_\venv\Scripts\python.exe C:\Users\********\PycharmProjects\Abstract_Reader_\main.py  

[BEGIN]  
Me: Determine whether this abstract 'In the paper an automated approach for construction of the terminological 
thesaurus for a specific domain is proposed. It uses an explanatory dictionary as the initial text corpus and a 
controlled vocabulary related to the target lexicon to initiate extraction of the terms for the thesaurus. 
Subdivision of the terms into semantic clusters is based on the CLOPE clustering algorithm. The approach 
diminishes the cost of the thesaurus creation by involving the expert only once during the whole construction 
process, and only for analysis of a small subset of the initial dictionary. To validate the performance of the 
proposed approach the authors successfully constructed a thesaurus in the cardiology domain.' from the paper 
'An approach to automated thesaurus construction using clusterization-based dictionary analysis'.Describes, 
includes or relates to 'generating or extracting a collection of related words', you must start your answer 
with the word 'yes' or 'no' and then your detailed reasoning.'  
text-davinci-003: Yes. The abstract describes an automated approach for constructing a terminological thesaurus 
for a specific domain, which involves extracting terms from an explanatory dictionary and then using a clustering 
algorithm to subdivide the terms into semantic clusters. This process of generating or extracting a collection of 
related words is a key part of thesaurus construction.  
[END]  

[BEGIN]  
Me: Determine whether this abstract 'To determine whether a document or a sentence expresses a positive or 
negative sentiment, three main approach types are commonly used: lexicon based approaches, machine learning 
(ML) based approaches and hybrid approaches. English has the greatest number of sentiment analysis studies, 
unlike other languages including Arabic and its dialects. More specifically, ML based sentiment analysis 
requires annotated data. In the case of lexicon based approaches, they typically require the availability 
of lexicons annotated by valence and/or intensity. One of the majors problems related to the treatment of 
Arabic and its dialect is the lack of the above resources. This survey is aimed to highlight the most recent 
resources that have been constructed and most recent advances in the context of sentiment analysis (related to 
English and Arabic language). It refers to about one hundred recent papers, most of which published between 2015 
and 2018. These works are classified by category (as survey work vs. solution work). In the case of solution works, 
we focus on the construction of sentiment lexicon and corpus. We also propose new trends in Arabic sentiment analysis, 
mainly employing deep learning techniques.' from the paper 'English vs Arabic Sentiment Analysis: A Survey Presenting 
100 Work Studies, Resources and Tools'.Describes, includes or relates to 'generating or extracting a collection of 
related words', you must start your answer with the word 'yes' or 'no' and then your detailed reasoning.'  
text-davinci-003: No. The abstract does not describe, include, or relate to generating or extracting a collection of 
related words. It instead describes the three main approaches used to determine whether a document or sentence expresses a 
positive or negative sentiment, the lack of resources for Arabic sentiment analysis, and the survey of 100 recent papers 
related to English and Arabic sentiment analysis.  
[END] 

Process finished with exit code 0

## Author
* Lee Taylor