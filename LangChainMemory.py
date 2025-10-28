
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


# Instalar si hace falta:
# %pip install -U langchain langchain-openai

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser

# LLM (requiere OPENAI_API_KEY en el entorno)
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)
to_str = StrOutputParser()

# Prompt con hueco para el historial
prompt = ChatPromptTemplate.from_messages([
    ("system", "Eres un asistente educativo claro y conciso."),
    MessagesPlaceholder("chat_history"),      # ← aquí va la memoria
    ("human", "{input}")
])

# Cadena base
chain = prompt | llm | to_str

# Memoria simple como lista de mensajes
history: list = []

def chat(user_text: str) -> str:
    """
    Envía un turno del usuario, usa el historial y actualiza la memoria
    con el par (usuario, asistente).
    """
    global history
    # Ejecutar la cadena inyectando el historial actual
    answer = chain.invoke({"input": user_text, "chat_history": history})
    # Actualizar memoria (guardar los dos mensajes)
    history += [HumanMessage(content=user_text), AIMessage(content=answer)]
    return answer

# --- Ejemplo de uso (tres turnos) ---
print(chat("Hola, soy un profesor de informática."))
print(chat("¿Puedes explicarme cómo introducir IA a mis estudiantes?"))
print(chat("¿Qué ejemplos prácticos puedo usar en la clase?"))

