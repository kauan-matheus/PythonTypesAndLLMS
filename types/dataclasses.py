# O que é self?
# self é a instância atual do objeto. Ele é usado para acessar variáveis que pertencem à classe
#  e para chamar outros métodos da classe. Ele é o primeiro parâmetro de todos os métodos
#  em uma classe, mas não precisa ser passado quando você chama o método.

class Usuario:
    def __init__(self, id: int, nome: str, ativo: bool):
        self.id = id
        self.nome = nome
        self.ativo = ativo

# Type hints NÃO protegem runtime e não impedem que você atribua um valor de tipo diferente a uma variável.
# Eles são apenas anotações para ajudar os desenvolvedores a entender o tipo de dado que uma variável
# deve conter e para fornecer informações de tipo para ferramentas de análise estática, como linters e IDEs.
# Por exemplo, mesmo que tenhamos definido o tipo de dado para a variável "usuario" como "Usuario",
# ainda podemos atribuir um valor de tipo diferente a essa variável, como uma string ou um número,
# e o Python não gerará um erro em tempo de execução.

usuario: Usuario = Usuario(1, "kauan", True) # Isso é válido

#  # Isso também é válido, mas não é recomendado, pois viola a intenção do tipo hint
#  e pode levar a erros em tempo de execução se o código tentar acessar atributos
#  ou métodos que não existem em uma string.
usuario = "Isso é uma string, não um objeto Usuario"


 ## ---CLASSES SEM DATACLASS--- ##
# Classes são usadas para criar objetos que possuem atributos (variáveis) e métodos (funções
class Usuario:
    # O método __init__ é um método especial que é chamado quando um objeto é criado a partir da classe.
    # Ele é usado para inicializar os atributos do objeto.
    def __init__(self, id: int, nome: str, ativo: bool):
        # O self é a instância atual do objeto, e é usado para acessar os atributos e métodos da classe.
        self.id = id
        self.nome = nome
        self.ativo = ativo

    # Métodos são funções definidas dentro de uma classe que operam em instâncias dessa classe.
    # Eles podem acessar e modificar os atributos do objeto usando o self.
    def desativar(self) -> None:
        self.ativo = False

    # O método esta_ativo é um método que retorna o valor do atributo ativo, indicando se o usuário está ativo ou não.
    def esta_ativo(self) -> bool:
        return self.ativo
    
## ---CLASSES COM DATACLASS--- ##
# Python automaticamente cria:
# - O método __init__ para inicializar os atributos
# - O método __repr__ para fornecer uma representação legível do objeto
# - O método __eq__ para comparar objetos com base em seus atributos
# E muito mais, dependendo dos parâmetros que você fornece ao dataclass.
from dataclasses import dataclass

@dataclass
class Usuario:
    id: int
    nome: str
    email: str
    ativo: bool

# Imutabilidade
# Ao usar @dataclass(frozen=True), você torna a classe imutável, o que significa que
# os atributos do objeto não podem ser modificados após a criação do objeto.
# Muito usado para:
#Configurações
#DTOs
#Eventos
@dataclass(frozen=True)
class Usuario:
    id: int
    nome: str


from typing import Literal
@dataclass
class Tarefa:
    id: str
    title: str
    status: Literal["pendente", "em_andamento", "concluida"]
    priority: int
    assigned_to: str | None