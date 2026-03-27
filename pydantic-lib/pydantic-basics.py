from pydantic import BaseModel
# o pydantic é uma biblioteca de validação de dados que usa modelos baseados em classes
# para definir a estrutura dos dados e validar os tipos de dados. 
# Ele é amplamente utilizado para criar APIs, validar dados de entrada e saída, 
# e garantir a integridade dos dados em aplicações Python.
# Ele é especialmente útil para trabalhar com dados que vêm de fontes externas, como APIs, arquivos

class Usuario(BaseModel):
    id: int
    nome: str
    saldo: float
    ativo: bool

# O pydantic automaticamente valida os tipos de dados e lança erros se os dados não corresponderem aos tipos definidos no modelo.
# Ele também suporta recursos avançados, como validação personalizada, conversão de tipos
# e integração com outras bibliotecas, como FastAPI para criação de APIs.
## Isso se chama coercion ##
usuario = Usuario(id=1, nome="kauan", saldo=100.0, ativo=True)
print(usuario)
    

## ---EXEMPLO REAL DE USO EM API--- ##

## Temos esse json aqui, e para usarmos ele na aplicação, usamos o pydantic
# {
#   "id": "uuid",
#   "title": "Mapear processo",
#   "status": "pendente",
#   "priority": 1,
#   "assigned_to": null
# }

## Modelo de dados para a tarefa
from pydantic import BaseModel
from typing import Literal

class Task(BaseModel):
    id: str
    title: str
    status: Literal["pendente", "em_andamento", "concluida"]
    priority: int
    assigned_to: str | None = None # esse campo pode ser opcional e pode ser nulo, por isso usamos str | None e atribuímos None como valor padrão.

# aqui eu crio uma instância do modelo Task usando os dados do JSON, e o pydantic irá validar
# os tipos de dados e garantir que eles correspondam ao modelo definido.
task = Task(
    id="123",
    title="Financeiro",
    status="pendente",
    priority=1
)

# O método model_dump() é usado para converter a instância do modelo em um dicionário,
# o que é útil para serializar os dados
task.model_dump()
print(task.priority)
