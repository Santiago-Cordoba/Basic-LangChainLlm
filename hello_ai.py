import os
from openai import OpenAI
from dotenv import load_dotenv
# Cargar variables de entorno
load_dotenv()
# Inicializar cliente con la clave API
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# Solicitud al modelo
for t in [0.1, 0.5, 0.9]:
 response = client.chat.completions.create(
 model="gpt-4o-mini",
 messages=[{"role": "user", "content": "Describe brevemente qué es la IA."}],
 temperature=t,
 max_tokens=50
 )
 print(f"--- temperature={t} ---")
 print(response.choices[0].message.content)
