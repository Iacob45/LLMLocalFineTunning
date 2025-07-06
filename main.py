from openai import AsyncOpenAI, OpenAI
import instructor
import time
from dotenv import load_dotenv
import asyncio
import datetime as dt
from models.DataModels import *
import requests



async def openAIProcessing(content, dataModel):
    print("Using OpenAI")
    load_dotenv()
    start = time.time()
    client = instructor.from_openai(AsyncOpenAI())
    try:
        response = await client.chat.completions.create(
            model='gpt-4o',
            max_retries=10,
            messages=[
                {
                    "role": "user",
                    "content": content
                }
            ],
            response_model=dataModel
        )
    except Exception as e:
        end = time.time()
        duration = end - start
        print(f"OpenAI's model gpt-4o failed to produce a response after {duration} s. Error: {e}")
        return [], duration
    end = time.time()
    duration = end - start
    return response

def ollamaProcessing(content, dataModel, ollamaModel):
    print(ollamaModel)
    start = time.time()
    client = instructor.from_openai(
        OpenAI(
            base_url='http://localhost:11434/v1',
            api_key='ollama'
        ),
        mode=instructor.Mode.JSON
    )
    try:
        response = client.chat.completions.create(
            model=ollamaModel,
            max_retries=10,
            messages=[
                {
                    "role": "user",
                    "content": content
                }
            ],
            response_model=dataModel
        )

    except Exception as e:
        end = time.time()
        duration = end - start
        print(f"Ollama model {ollamaModel} failed to produce a response after {duration} s.")
        return [], duration
    end = time.time()
    duration = end - start
    return response, duration

async def main():
    print("App starting")
    content1 = (f'Leonardo was born on April 4th 1990. Today is {dt.date.today()}.'
               f' Fill the data model based on this information.')
    content2 = (f'I love Shutter Island. It is one of my favorite movies of all time.'
                f' Recommend 5 more that are similar.')


    for model in ollamaModels.values():
        responseOllama, processing_time = ollamaProcessing(content=content2, dataModel=MovieResponseModel, ollamaModel=model)
        if responseOllama:
            print(f"Response using Ollama model {model} in {processing_time}s: {responseOllama}")







if __name__ == "__main__":
    asyncio.run(main())
