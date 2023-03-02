"""
# Author: Lee Taylor
The purpose of this project is to speed up a bibliographic review of literature.
Please the view the README.md for more information.
"""
import os
import openai
import api_key  # Create a file called
import pandas as pd
import csv


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
           f" you must start your answer with the word 'yes' or 'no' with a fullstop " \
           f"and then your detailed reasoning.'"


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


def write_to_csv(filename, data):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)


if __name__ == '__main__':
    # Extract columns into lists
    cols_ = extract_cols(['Document Title', 'Abstract', 'PDF Link'])

    # Define user-topic
    user_topic_ = f'generating or extracting a collection of related words'

    # Storage for .csv writer
    data_r1, data_r2 = [], []

    # Generate response for each pair
    for i, v in enumerate(cols_):
        # Extract: title, abstract, ...
        title_, abstract_, pdf_link = v
        # Create prompt
        prompt_1 = create_prompt(title_, abstract_, 1, user_topic_)
        prompt_2 = create_prompt(title_, abstract_, 2, user_topic_)
        # Generate response
        res_1 = gen_response(prompt_1)
        res_2 = gen_response(prompt_2)
        # Out response
        # print_fio(prompt_, res_)
        # Update storage for later to write to .csv
        data_r1.append([response_text(res_1).strip().split()[0], title_, abstract_, pdf_link])
        data_r1.append([response_text(res_2).strip().split()[0], title_, abstract_, pdf_link])

    # Todo: Generate a .csv file with the first column being the 'yes' or 'no'
    #  from the text-davinci-003 model response

    # Write to .csv file
    write_to_csv('output_r1.csv', data)

