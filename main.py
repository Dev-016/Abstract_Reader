"""
# Author: Lee Taylor
The purpose of this project is to speed up a bibliographic review of literature.
Please the view the README.md for more information.
"""
import os
import openai
import api_key
import pandas as pd


# Load your API key from an environment variable or secret management service
openai.api_key = api_key.API_KEY

# Define excel file to parse
fd = "Excels/Lexicon_Construction.xlsx"


def extract_cols(col_names):
    df = pd.read_excel(fd)
    cols, extracted = [], []
    for col in col_names:
        cols.append(df[col].tolist())
    for i in range(len(cols[0])):
        extracted.append([arr[i] for arr in cols])
    # print(extracted)
    return extracted


def create_prompt(title, abstract, r_strength=1, user_topic=f'generating or extracting a collection of related words'):
    if 1 > r_strength > 2:
        raise ValueError('Parameter r_strength should equal 1 or 2.')
    r_strength_str = ''
    # Determine the strength of the relationship between the abstract and user topic
    if r_strength == 1:
        r_strength_str = 'Describes, includes or relates to '
    elif r_strength == 2:
        r_strength_str = 'Is directly related to '
    # Form and return prompt as a string
    return f"Determine whether this abstract '{abstract}' from the paper '{title}'." \
           f" {r_strength_str} '{user_topic}'," \
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
          f"Me: {prompt}\n\n"
          f"text-davinci-003: {response_text(res).strip()}\n"
          f"[END]\n")


if __name__ == '__main__':
    # Extract columns into lists
    cols_ = extract_cols(['Document Title', 'Abstract', 'PDF Link'])

    # Define user-topic
    user_topic_ = f'generating or extracting a collection of related words'

    # Generate response for each pair
    for i, v in enumerate(cols_):
        title_, abstract_, pdf_link = v
        prompt_ = create_prompt(title_, abstract_, 1, user_topic_)
        res_ = gen_response(prompt_)
        print_fio(prompt_, res_)
        cols_.append(response_text(res_).strip().split()[0])

    # Todo: Generate a .csv file with the first column being the 'yes' or 'no'
    #  from the text-davinci-003 model response
