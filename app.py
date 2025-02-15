##########
#@@@@@@@@@

import os
import logging
from decouple import config
from fastapi import FastAPI
from langchain_groq import ChatGroq
#from langchain_openai import ChatOpenAI
from langserve import add_routes
from chains import get_translate_chain

# 1. Configurações de Log
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("fastapi")

# 2. Mensagens de log de exemplo
logger.info('Iniciando o script apptranslate.py (log fora de qualquer evento).')

#os.environ['OPENAI_API_KEY'] = config('OPENAI_API_KEY')
os.environ['GROQ_API_KEY'] = config('GROQ_API_KEY')

# 3. Instância do FastAPI
app = FastAPI(
    title='Tradutor Groq',
    version='1.01',
    description='Projeto API - Prof. Rogério',
    summary='API para tradução de texto',
    terms_of_service="https://expertatech.com.br/termos//",
    contact={
        "name da equipe": "LL-Leandro Lima, RK -Ricardo Kerr, ML - Marcu Loreto",
        "url": "http://github.com/rogerior/",
        "emails": "Leandrowaglima@gmail.com , ricardo.kerr@gmail.com , mlbonfim@gmail.com",
    },
)

# 4. Evento de STARTUP
@app.on_event("startup")
def startup_event():
    logger.info("Evento de startup: API iniciando...")

# 5. Evento de SHUTDOWN
@app.on_event("shutdown")
def shutdown_event():
    logger.info("Evento de shutdown: API finalizando...")

# Exemplo de modelos, se você desejar expô-los
#openai_model = ChatOpenAI(model='gpt-4o')
groq_model = ChatGroq(model='llama-3.3-70b-versatile')

# Rota customizada (chainstranslate)
add_routes(
    app,
    get_translate_chain(),
    path='/translate',
)
