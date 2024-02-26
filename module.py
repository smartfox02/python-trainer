import openai
from gpt_index import SimpleDirectoryReader, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
# import gpt_index
from langchain.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def chatbot(input_text):
    index = GPTSimpleVectorIndex.load_from_disk('index.json')
    response = index.query(input_text, response_mode="compact")
    partial_message = ""
    for chunk in response.response:
        partial_message = partial_message + chunk
        # yield partial_message
    return partial_message 
