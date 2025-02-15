# Tradutor Groq

API desenvolvida em **FastAPI** para traduzir textos utilizando **Langchain** e **Groq**.
Fazemos uso de cadeias (chains) para formatar o prompt, interagir com o modelo e processar a saída.

---

## Sumário
- [Descrição](#descrição)
- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Uso](#uso)
- [Logs](#logs)
- [Autores](#autores)

---

## Descrição
Este projeto disponibiliza um endpoint `/translate` para receber um objeto JSON e traduzir o texto informado para o idioma de destino. Utiliza-se o modelo **llama-3.3-70b-versatile** via **ChatGroq**.

---

## Requisitos
- **Python 3.10+**
- **FastAPI**
- **Uvicorn**
- **OpenAI API Key**
- **Groq API Key**

Todas as dependências estão listadas em [requirements.txt](./requirements.txt).

---

## Instalação
1. **Clonar** o repositório:
   ```bash
   git clone https://github.com/SEU_USUARIO/API_POS.git
   cd API_POS
   ```
2. **Criar um ambiente virtual** (recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```
3. **Instalar** as dependências:
   ```bash
   pip install -r requirements.txt
   ```

---

## Configuração
Crie um arquivo `.env` na raiz do projeto com as variáveis:

```ini
OPENAI_API_KEY=sk-...
GROQ_API_KEY=groq-...
```

Substitua pelos valores reais das suas chaves de API.

---

## Uso
1. **Executar** a aplicação (via Uvicorn):
   ```bash
   uvicorn app:app --reload
   ```
2. Acesse [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) para ver a **documentação interativa** e testar o endpoint `/translate`.

Exemplo de `POST /translate`:
```json
{
  "language": "en",
  "text": "Olá, mundo!"
}
```

---

## Logs
- O projeto utiliza **logging** para exibir mensagens no console, com diferentes níveis (INFO, WARNING, ERROR, CRITICAL).  
- Você verá as mensagens assim que iniciar o servidor, ou quando ocorrerem eventos de startup/shutdown.

---

## Autores
- **Prof. Rogério** (Orientador)
- **LL (Leandro Lima)**
- **RK (Ricardo Kerr)**
- **ML (Marcu Loreto)**


Esperamos que seja útil! Qualquer dúvida, abra uma [issue](https://github.com/SEU_USUARIO/API_POS/issues). 🚀

