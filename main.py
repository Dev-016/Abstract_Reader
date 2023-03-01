# Author: Lee Taylor
import os
import openai
import api_key
import pandas as pd


# Load your API key from an environment variable or secret management service
openai.api_key = api_key.API_KEY


'''
The purpose of this project is to speed up a bibliographic review of literature. 
Please the view the README.md for more information.
'''


def extract_ta_pairs():
    """
    This function reads the .xlsx into a dataframe (DF).
    The paper titles and abstracts are extracted from the DF into
     a list of tuple pairs.
    """
    df = pd.read_excel("Excels/Lexicon_Construction.xlsx")
    doc_title = df['Document Title'].tolist()
    abstracts = df['Abstract'].tolist()
    return [(t, a) for t, a in zip(doc_title, abstracts)]


def create_prompt(title, abstract):
    user_topic = f'generating or extracting a collection of related words'
    return f"Determine whether this abstract '{abstract}' from the paper '{title}'." \
           f" Describes, includes or relates to '{user_topic}'," \
           f" you must start your answer with the word 'yes' or 'no' and then your detailed reasoning.'"


def gen_response(prompt):
    response = openai.Completion.create(model="text-davinci-003",
                                        prompt=prompt,
                                        temperature=0,
                                        max_tokens=2000)
    return response


def response_text(response):
    return response["choices"][0]["text"]


def print_fio(prompt, res):
    print(f"[BEGIN]\n"
          f"Me: {prompt}\n"
          f"text-davinci-003: {response_text(res).strip()}\n"
          f"[END]\n")


if __name__ == '__main__':
    # Test Response
    # prompt_ = "What is 2+2?"
    # res_ = gen_response(prompt_)
    # print_fio(prompt_, res_)

    # Title-Abstract pairs
    pairs = extract_ta_pairs()

    # Generate response for each pair
    for title, abstract in pairs[80:90]:
        prompt_ = create_prompt(title, abstract)
        res_ = gen_response(prompt_)
        print_fio(prompt_, res_)
