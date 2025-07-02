from openai import OpenAI
import instructor
from dotenv import load_dotenv
import datetime as dt
from models.DataModels import *




def openAIProcessing(content, dataModel):
    print("Using OpenAI")
    load_dotenv()
    client = instructor.from_openai(OpenAI())
    response = client.chat.completions.create(
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
    return response

def ollamaProcessing(content, dataModel, ollamaModelIndex):
    print("Using Ollama")

    ollamaModels= {0:'llama2:latest',
                   1:'llama3.2:latest',
                   2:'deepseek-coder-v2:16b',
                   3:'gemma3:12b',
                   4:'gemma3:27b',
                   5:'llama3.2:3b'}
    client = instructor.from_openai(
        OpenAI(
            base_url='http://localhost:11434/v1',
            api_key='ollama'
        ),
        mode=instructor.Mode.JSON
    )
    response = client.chat.completions.create(
        model=ollamaModels[ollamaModelIndex],
        max_retries=10,
        messages=[
            {
                "role": "user",
                "content": content
            }
        ],
        response_model=dataModel
    )
    return response

def main():
    print("App starting")
    content = (f'Leonardo was born on April 4th 1990. Today is {dt.date.today()}.'
               f' Fill the data model based on this information.')


    # responseOpenAI = openAIProcessing(content,model)
    # print("Response from OpenAI:\n", responseOpenAI)

    responseOllama = ollamaProcessing(content=content,dataModel=Caption,ollamaModelIndex=0)
    print("Response from Ollama:\n",responseOllama)
    responseOllama = ollamaProcessing(content=content, dataModel=Caption, ollamaModelIndex=1)
    print("Response from Ollama:\n", responseOllama)
    responseOllama = ollamaProcessing(content=content, dataModel=Caption, ollamaModelIndex=2)
    print("Response from Ollama:\n", responseOllama)





if __name__ == "__main__":
    main()
