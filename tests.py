from main import *


def test_response():
    prompt_ = "What is 2+2?"
    res = gen_response(prompt_)
    print(f">>> BEGIN: \n"
          f"Me: {prompt_}\n"
          f"text-davinci-003: {response_text(res).strip()}")


if __name__ == '__main__':
    # test_response()
    pass
