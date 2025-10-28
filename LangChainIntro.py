
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()  # Cargar archivo .env
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("No se encontró la clave OPENAI_API_KEY en el archivo .env")

# Crear cliente LangChain con OpenAI
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)
print("Cliente LangChain con OpenAI inicializado correctamente.")

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Initialize the LLM (uses your OpenAI API key from environment)
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)

# Create a simple prompt
prompt = ChatPromptTemplate.from_template(
    "Explica en dos frases el concepto de {tema}."
)

# Combine the components using LCEL (LangChain Expression Language)
chain = prompt | llm | StrOutputParser()

# Run it
result = chain.invoke({"tema": "aprendizaje automático"})
print(result)

