from fastapi import FastAPI, Body, HTTPException
import os
from model.dataOpenAi import dataOpenApi
from service.apiopenai import OpenAirequest
from fastapi.middleware.cors import CORSMiddleware
from service.opeaiwithshortcontext import OpenAiContextShort
from starlette.responses import JSONResponse
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
        openai.updateContext()
        openai.fileClose()
        return data
openapiwithcontext=OpenAiContextShort()
@app.post("/chatapiwithshortcontext/")
async def create_item(item: dataOpenApi):
        try:
            data=openapiwithcontext.requestApi(item.prompt)
            return JSONResponse(status_code=200, content={"message": data})
        except Exception as e:
           return JSONResponse(status_code=500, content={"message": "Error in OpenAi Api"})


