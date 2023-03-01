import os
import openai
import api_key
import pandas as pd


# Load your API key from an environment variable or secret management service
openai.api_key = api_key.API_KEY


'''
def read_excel(file_path):
    df = pd.read_excel("Excels/Lexicon_Construction.xlsx")
    print(df)
'''


def read_excel():
    df = pd.read_excel("Excels/Lexicon_Construction.xlsx")
    doc_title = df['Document Title'].tolist()
    abstracts = df['Abstract'].tolist()
    pairs = [(t, a) for t, a in zip(doc_title, abstracts)]
    for pair in pairs:
        print(pair)


def extract_title():
    pass


def extract_abstract():
    pass


def create_prompt():
    pass


def gen_response(prompt):
    response = openai.Completion.create(model="text-davinci-003",
                                        prompt=prompt,
                                        temperature=0,
                                        max_tokens=2000)
    return response


def response_text(response):
    return response["choices"][0]["text"]


def print_fio(prompt, res):
    print(f">>> BEGIN: \n"
          f"Me: {prompt}\n"
          f"text-davinci-003: {response_text(res).strip()}")


if __name__ == '__main__':
    # Test Response
    # prompt_ = "What is 2+2?"
    # res_ = gen_response(prompt_)
    # print_fio(prompt_, res_)

    # Test reading
    read_excel()
