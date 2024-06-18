from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langserve import add_routes
from dotenv import load_dotenv
import os

load_dotenv()
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# system_prompt_template = "Translate the following into {language}"
# promp_template = ChatPromptTemplate.from_messages(
#     [("system", system_prompt_template),
#     ("user" , "{text}")]
# )

# model = ChatOpenAI(model = "gpt-3.5-turbo")
# parser = StrOutputParser()
# chain = promp_template | model | parser
# # res = chain.invoke({"language" : "italian",
# #               "text": "Hi"})

# app = FastAPI( title= "Langchain server" , version= "1.0" , description= " Simple API server using Langchain's Runnable Intrface")
# add_routes( app , runnable= chain , path= "/chain")
# import uvicorn
# if __name__ == "__main__":   
#     uvicorn.run(app , host= "localhost" , port = 8000)

#!/usr/bin/env python
from typing import List

from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langserve import add_routes

# 1. Create prompt template
system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{text}')
])

# 2. Create model
model = ChatOpenAI()

# 3. Create parser
parser = StrOutputParser()

# 4. Create chain
chain = prompt_template | model | parser


# 4. App definition
app = FastAPI(
  title="LangChain Server",
  version="1.0",
  description="A simple API server using LangChain's Runnable interfaces",
)

# 5. Adding chain route

add_routes(
    app,
    chain,
    path="/chain",
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)