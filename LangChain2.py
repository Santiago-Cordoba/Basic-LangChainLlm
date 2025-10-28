
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
from operator import itemgetter

# 1) LLM (usa tu OPENAI_API_KEY en el entorno)
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)
to_str = StrOutputParser()

# 2) Paso 1: explicar brevemente el concepto de {tema}
primer_prompt = ChatPromptTemplate.from_template(
    "Explica brevemente el concepto de {tema}."
)
primer_paso = primer_prompt | llm | to_str
# `primer_paso` produce un string, por ejemplo: "La realidad aumentada es ..."

# 3) Paso 2: proponer una aplicación educativa usando la salida del paso 1 como {concepto}
segundo_prompt = ChatPromptTemplate.from_template(
    "Propón una aplicación educativa del siguiente concepto: {concepto}."
)
segundo_paso = segundo_prompt | llm | to_str

# 4) Encadenar: mapear la entrada {tema} al primer paso, y su salida a {concepto} del segundo
cadena_secuencial = {"concepto": primer_paso} | segundo_paso

# 5) Ejecutar la cadena completa
resultado = cadena_secuencial.invoke({"tema": "realidad aumentada"})
print(resultado)