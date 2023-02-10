from fastapi import FastAPI, Body
from model.dataOpenAi import dataOpenApi
from service.apiopenai import OpenAirequest
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
openai=OpenAirequest()
@app.post("/chatapi/")
async def create_item(item: dataOpenApi):
        openai.openFile()
        openai.requestApi(item.prompt)
        data=openai.writeResponse()
        print(data)
        openai.updateContext()
        openai.fileClose()
        return data

