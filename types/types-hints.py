## ---TIPOS DE DADOS COM HINTS--- ##

## Primitivos
idade: int = 21
saldo: float = 100.0
ativo: bool = True
nome: str = "kauan"

## Coleções
#mutavel, eu posso alterar os elementos
tags: list[str] = ["python", "tipagem", "hints"]
tags.append("comercial")

## Tuples (imutáveis)
coordenada: tuple[int, int] = (10, 20)
coordenada[0] # 10
# coordenada[0] = 15 # Erro, não é possível alterar uma tupla pq é imutavel

## Dicionário (dict)
usuario: dict[str, str] = {
    "Nome": "kauan",
    "Email": "kauan8643@gmail.com"
}

#ou mais realista
usuario: dict[str, str | int | bool] = {
    "Nome": "kauan",
    "Email": "kauan8643@gmail.com",
    "Idade": 21,
    "Ativo": True
}

## Set (conjunto de elementos únicos, nn permite elementos duplicados)
numeros: set[int] = {1, 2, 3, 4, 5}
numeros.add(6) #Aqui eu posso adicionar pq n existe no set
numeros.add(3) #Aqui n vai adicionar pq o 3 já existe no set

## Tipos Especiais (None)
#None é usado para indicar a ausência de valor
resultado: None = None

#em função
def processar_dados(dados: str) -> None:
    ... # Processa os dados

## Union (tipos alternativos)
#Pode ser int ou string
valor: int | str = 42
valor = "quarenta e dois" # Agora é uma string, mas ainda é válido

#Optional (pode ser do tipo ou None)
idade: int | None # Pode ser um inteiro ou None
idade = 30 # Válido
idade = None # Também é válido, indicando que a idade não foi fornecida

## ---Any (qualquer tipo)--- ##
from typing import Any
# Any é um tipo especial que pode representar qualquer tipo de dado. 
# Ele é útil quando você não tem certeza do tipo de dado que será usado
# ou quando deseja permitir flexibilidade total.
variavel: Any = 42
variavel = "Agora é uma string"
variavel = [1, 2, 3]

## ---EXEMPLO DE USO DE TIPOS--- ##
def listar_tarefas() -> list[dict[str, str | int | bool]]:
    return [
        {"id": 1, "tarefa": "financeiro", "concluida": False},
        {"id": 2, "tarefa": "marketing", "concluida": True}
    ]
