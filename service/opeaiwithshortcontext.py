import os
import re
import openai
class OpenAiContextShort:
    openai.api_key = "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"
    context = []
    response = ""
    def get_last_5_summary_chats(self,chats):
        res =''
        for index, question_response in enumerate(chats[-5:]):
            res+= f"prompt{index}: {question_response[0]} response{index}: {question_response[1]} "
        if(len(chats)> 3):
            res = "Give short responses only."+ res
        return res

    def requestApi(self, prompt):
            for ind in range(10):
                prev_context = self.get_last_5_summary_chats(self.context)
                response = openai.Completion.create(
                model="text-davinci-003",
                prompt=prev_context + "\n\n"+ prompt,
                temperature=0.7,
                max_tokens=400,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
        )
                self.context.append([prompt, response["choices"][0]["text"]])
            
                return re.sub("[A-Za-z]+[0-9]+ \?","",response["choices"][0]["text"]) + "\n"

    
        
