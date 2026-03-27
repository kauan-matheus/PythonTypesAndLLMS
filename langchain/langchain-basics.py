# -- LangChain é um framework para construir aplicações com LLMs (como GPT) -- #

# Ele serve para:

# Criar agentes
# Conectar LLM com banco
# Conectar LLM com API
# Criar ferramentas (tools)
# Controlar memória
# Forçar saída estruturada

# Não é IA.
# É infraestrutura para usar IA.

# Quando você usa um LLM puro (tipo OpenAI API), você só manda texto:

# "Resuma esse texto"

# Mas em sistemas reais você precisa:

# Buscar dados no banco
# Validar saída
# Chamar API
# Executar função
# Forçar formato JSON

# LangChain organiza isso.


# Modelo de linguagem #
## aqui eu to definindo qual llm eu quero usar, e o LangChain vai cuidar de toda a infraestrutura
# para me permitir usar esse modelo de forma fácil e eficiente.
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-4")

# Aqui eu to criando um prompt, que é basicamente uma instrução ou pergunta que eu quero fazer para o modelo de linguagem.
# O ChatPromptTemplate é uma classe do LangChain que me permite criar prompts de forma estruturada,
# usando placeholders para inserir variáveis dinamicamente. 
from langchain.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_template("Resuma esse texto: {texto}")

# -- CHAIN -- #

# Conecta prompt + LLM.
# Fluxo:
# Input → Prompt → LLM → Output

from pydantic import BaseModel
from typing import Literal

class AnaliseFinanceira(BaseModel):
    risco: Literal["baixo", "medio", "alto"]
    resumo: str

# O que é um Agent?

# Um Agent é um LLM que pode:

# Raciocinar
# Escolher ferramenta
# Executar ação
# Observar resultado
# Decidir próximo passo