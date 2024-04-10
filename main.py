from langchain.chains import LLMChain
from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
import os


template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])

llm = OpenAI()

llm_chain = LLMChain(prompt=prompt, llm=llm)

question = "¿Quién fue el primero en hablar sobre la inteligencia artificial?"

response = llm_chain.run(question)
print(response)
