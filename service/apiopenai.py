import openai
import re
import os
class OpenAirequest:
    openai.api_key = "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"
    model_engine = "text-davinci-003"
    topic = "airesearchproject"
    prompt = ""
    context = ""
    history_log = re.sub('[^0-9a-zA-Z]+', '', topic) + '.log'
    def openFile(self):
        self.file = open(self.history_log, "a")
        return
    def requestApi(self, prompt):
            self.prompt = prompt
            self.file.write(self.prompt)
            self.response = openai.Completion.create(
                model="text-davinci-003",
                prompt=self.context + "\n\n"+ self.prompt,
                temperature=0.7,
                max_tokens=4000,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
        )
    def writeResponse(self):
        self.file.write(self.response["choices"][0]["text"] + "\n")
        print("context: ", self.context)
        return self.response["choices"][0]["text"] + "\n"
    def updateContext(self):
        self.context += "\n".join([self.context, self.prompt, self.response["choices"][0]["text"]])
        return self.context
    def fileClose(self):
        self.file.close()
        return
