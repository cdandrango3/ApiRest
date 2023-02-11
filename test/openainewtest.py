import re, requests, os
env = os.environ


public_end_point = 'https://api.openai.com/v1/completions'
headers = {'authorization': f"Bearer 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"}

#This function provides the context. Note that that it will consume a lot of tokens (input tokens)
def get_last_5_summary_chats(chats):
    res =''
    for index, question_response in enumerate(chats[-5:]):
        res+= f"prompt{index}: {question_response[0]} response{index}: {question_response[1]} "
    if(len(chats)> 3):
        res = "Give short responses only."+ res
    return res

#Store your chat history in session_chats
session_chats = []

#Set Input Parameters to the endpoint
data = { "model": 'text-davinci-003', "max_tokens": 400, "temperature": 1, "top_p": 0.6}

for ind in range(10):
    prev_context = get_last_5_summary_chats(session_chats)
    prompt = input("Ask your question:\t").strip()
    data['prompt'] = f"{prev_context} {prompt}".strip()
    r = requests.post(public_end_point, headers=headers, json=data)
    public_response = r.json()
    response_text = public_response['choices'][0]['text'].strip()
    print(f"QUESTION:\t{prompt}\n")
    print(f"RESPONSE:\t {response_text}\n\n")
    session_chats.append([prompt, response_text])
