###########

import os
import logging
from decouple import config

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
#from langchain_openai import ChatOpenAI

# Configurações de Log
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("chainstranslate")

logger.info('Mensagem informativa')
logger.warning('Mensagem de alerta')
logger.error('Mensagem de erro')
logger.critical('Mensagem crítica')

#os.environ['OPENAI_API_KEY'] = config('OPENAI_API_KEY')
os.environ['GROQ_API_KEY'] = config('GROQ_API_KEY')

# Exemplo de modelos, se você desejar expô-los
# openai_model = ChatOpenAI(model='gpt-4o')
# groq_model = ChatGroq(model='llama-3.3-70b-versatile')

def get_translate_chain():
    model = ChatGroq(
        model='llama-3.3-70b-versatile',
    )
    translate_prompt = ChatPromptTemplate.from_template(
        'Traduza o texto a seguir para o idioma {language}: {text}'
    )
    translate_chain = translate_prompt | model | StrOutputParser()
    return translate_chain
