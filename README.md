# Abstract_Reader

The purpose of this project is to speed up a bibliographic review of literature. By passing the abstract of each paper 
from a list of papers and instructing an OpenAI text-completion/instruct model to 'Determine whether this abstract from 
the paper /TITLE/ describes or includes /THIS TOPIC/, you must start with the word 'yes' or 'no' in your answer.' The 
last sentence in our prompt enables the collection of model responses to be parsed for either word to classify whether 
a paper does or does not describe or include the user's intended topic. 

## Author
* Lee Taylor