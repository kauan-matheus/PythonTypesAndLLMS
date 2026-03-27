## ---LISTAS--- ##

#Listas python
task = ["financeiro", "marketing"]

#acessa por task[0]
task[0]

## ---DICIONÁRIO (dict)--- ##

#dicionário (dict)
usuario = {
    "id": 1,
    "nome": "kauan",
    "saldo": 100.0,
    "ativo": True
}

## ---LOOP--- ##
#Iterando sobre elementos
for tarefa in task:
    print(tarefa)

#Iterando sobre indice
for i in range (len(task)):
    print(task[i])

## ---FUNÇÕES--- ##
def somar(a,b):
    return a + b

#Função para verificar se a idade é maior ou igual a 18
def maior_de_idade(idade):
        return idade >= 18

maior_de_idade(20) #True
maior_de_idade(17) #False

## ---FUNÇÃO COM TIPAGEM HINT--- ##

# Não bloqueiam execução.
# São apenas anotações
# Esse -> bool, significa o tipo de retorn da função, nesse caso um booleano
def maior_de_idade_tipado(idade: int) -> bool:
    return idade >= 18

maior_de_idade_tipado(20) #True
maior_de_idade_tipado(17) #False

## ---MUTABILIDADE--- ##
lista1 = [1, 2, 3]
lista2 = lista1

lista2.append(4)

print(lista1) # [1, 2, 3, 4]
print(lista2) # [1, 2, 3, 4]