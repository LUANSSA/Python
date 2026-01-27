print("\n********** Lista **********")
# Listas
frutas = ["Laranja", "Banana", "Maçâ", "Goaiaba", "Acerola"]
vazia = []
letras = list("Academia")
numeros = list(range(20))
carro = ["RAM", "RAMPAGE R/T", 2025, "Esportivo", "R$ 274.990", 20]

print(f"{frutas}")
print(f"{vazia}")
print(f"{numeros}")
print(f"{carro}")

print("\n********** Lista ['A','c','a','d','e','m','i','a'] **********")
lista = list("Academia")
print("Exibe a lista na ordem")
print(lista)
print(lista[::])
print("Lista de trás para frente!")
print(lista[::-1])
print("Exibe da posição 2 até a posição final")
print(lista[2:])
print("Exibe da posição inicial até a posição 2 -1")
print(lista[:2])
print("Exibe da posição 1 até a posição 4 -1")
print(lista[1:4])
print("Exibe da posição 0 até a posição 8 -1 e pula 2 indices -> A c A d E m I a ")
print(lista[0:8:2])
print(len(lista))


print("\n********** Lista de frutas **********")
# Loop em lista de frutas
for fruta in frutas:
    print(fruta)

print("\n********** Lista de frutas com index **********")
# Loop com index em lista de frutas
for index, fruta in enumerate(frutas):
    print(f"index:{index} fruta:{fruta}")

print("\n********** Lista de números pares **********")
# Retorna os números pares
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

print("\n********** Cópia de Lista **********")
# Cópia de Lista
listaCopia = lista.copy()
print(listaCopia)
listaCopia.append("Y")
print(lista)
print(listaCopia)

print("\nConta quantas vezes um item da lista se repete 'a' e 'c'")
print(lista.count("a"))
print(lista.count("c"))

print("\nPega o index da primeira ocorrencia do item 'A' e 'c'")
print(lista.index("A"))
print(lista.index("c"))

print("\nJuntando duas listas")
lista.extend(listaCopia)
print(lista)
print(listaCopia)

print("\nRemovendo itens da lista com pop()")
# A lista pode se comportar como pilha
print(listaCopia)
listaCopia.pop() # Removeu o 'Y'
listaCopia.pop() # Removeu o 'a'
listaCopia.pop() # Removeu o 'i'
listaCopia.pop(0) # Removeu o item da index 0 'A'
print(listaCopia)

print("\nRemove a primeira ocorrência da letra 'a' .remove('a')")
# Remove a primeira ocorrencia do item
lista.remove("a")
print(lista)

print("\nInverte a lista e deixa de trás para frente .reverse()")
lista.reverse()
print(lista)

print("\n********** Ordenação de Lista **********")
# Ordenamento
linguaguens = ["python", "js", "c", "java", "c#"]
print(linguaguens)
print("\nOrdenação crescente .sort()")
# Ordena lista
linguaguens.sort()
print(linguaguens)
print("\nOrdenação decrescente .sort(reverse=True)")
# Ordena lista de forma reversa
linguaguens.sort(reverse=True)
print(linguaguens)

print("\n********** Ordenação de Lista com função anônima **********")
print("Ordenação com função anônima: Neste caso da menor string para maior string")
linguaguens.sort(key=lambda x: len(x))
print(linguaguens)

print("\nOrdenação com função anônima: Neste caso com 'reverse' a ordenação é do maior para o menor")
linguaguens.sort(key=lambda x: len(x), reverse=True)
print(linguaguens)


print("\nFunção de Ordenação Built in (Padrão do interpretador Python)")
print(sorted(linguaguens))
print(sorted(linguaguens, key=lambda x: len(x)))
print(sorted(linguaguens, key=lambda x: len(x), reverse=True))


print("\n********** Lista de Listas **********")
# Lista de listas - Matriz
listaAmigos = [
        ["Luan", "Salvador", "BA", 27],
        ["Álvaro", "Salvador", "BA", 29],
        ["Isadora", "Salvador", "BA", 30],
    ]

# Insere no final da lista uma nova lista
listaAmigos.append(["Gabriel", "Salvador", "BA", 28])
# Remove a primeira lista
listaAmigos.pop(0)
# Remove o segundo item da primeira lista
listaAmigos[0].pop(1)
# Insere uma nova lista na posição 1
listaAmigos.insert(1, ["Paulo", "Salvador", "BA", 54])

print("Listas:")
print(listaAmigos)

print("\nPrimeira lista das listas:")
print(f"{listaAmigos[0]}")
print(f"{listaAmigos[0][0]}")
print(f"{listaAmigos[0][1]}")

# O -1 exibe de trás para frente
print("\nLista das listas ao contrário -1:")
print(f"{listaAmigos[-1]}")
print(f"{listaAmigos[-1][0]}")
print(f"{listaAmigos[-1][2]}")
print(f"{listaAmigos[-1][-1]}")
