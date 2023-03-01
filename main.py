import openai
import api_key


# Load your API key from an environment variable or secret management service
openai.api_key = api_key.API_KEY


def gen_response(prompt):
    response = openai.Completion.create(model="text-davinci-003",
                                        prompt=prompt,
                                        temperature=0,
                                        max_tokens=2000)
    return response


def response_text(response):
    return response["choices"][0]["text"]


if __name__ == '__main__':
    prompt = "What is 2+2?"
    res = gen_response(prompt)
    print(f">>> BEGIN: \n"
          f"Me: {prompt}\n"
          f"text-davinci-003: {response_text(res).strip()}")
