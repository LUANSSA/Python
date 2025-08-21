# Listas
frutas = ["Laranja", "Banana", "Maçâ", "Goaiaba", "Acerola"]
vazia = []
letras = list("Academia")
numeros = list(range(20))
carro = ["RAM", "RAMPAGE R/T", 2025, "Esportivo", "R$ 274.990", 20]

# Matriz
matriz = [

    [1, "a", 2],
    ["b", 3, 4],
    [5, 6, "c"]
]

print(f"{frutas}")
print(f"{vazia}")
print(f"{letras}")
print(f"{numeros}")
print(f"{carro}")

print(f"{matriz}")
print(f"{matriz[0]}")
print(f"{matriz[0][0]}")
print(f"{matriz[0][1]}")

print(f"{matriz[-1]}")
print(f"{matriz[-1][0]}")
print(f"{matriz[-1][2]}")
print(f"{matriz[-1][-1]}")


lista = list("Academia")

print(lista[::])
print(lista[2:])
print(lista[:2])
print(lista[1:4])
print(lista[::-1])
print(len(lista))
print(lista[0:8:2])

# Loop em lista de frutas
for fruta in frutas:
    print(fruta)

# Loop com index em lista de frutas
for index, fruta in enumerate(frutas):
    print(f"index:{index} fruta:{fruta}")

# Retorna os números pares
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)


# Cópia de Lista
listaCopia = lista.copy()
print(lista)
print(listaCopia)
listaCopia.append("Y")
print(lista)
print(listaCopia)

# Conta quantas vezes um item da lista se repete
print(lista.count("a"))

# Pega o index da primeira ocorrencia do item
print(lista.index("A"))
print(lista.index("c"))

# Juntar listas
lista.extend(listaCopia)
print(lista)
print(listaCopia)

# A lista pode se comportar como pilha
lista.pop() # Removeu o 'Y'
lista.pop() # Removeu o 'a'
lista.pop() # Removeu o 'i'
lista.pop(0) # Removeu o item da index 0 'A'
print(lista)

# Conta quantas vezes um item da lista se repete
print(lista.count("a"))
# Remove a primeira ocorrencia do item
lista.remove("a")
print(lista.count("a"))
print(lista)
lista.reverse()
print(lista)