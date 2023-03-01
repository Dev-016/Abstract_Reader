from main import *


def test_response():
    prompt = "What is 2+2?"
    res = gen_response(prompt)
    print(f">>> BEGIN: \n"
          f"Me: {prompt}\n"
          f"text-davinci-003: {response_text(res).strip()}")


def test_extract_cols():
    extract_cols(['Document Title', 'Abstract', 'PDF Link'])


if __name__ == '__main__':
    # test_response()
    pass
