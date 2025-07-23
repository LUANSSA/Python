# Listas

frutas = ["Laranja", "Banana", "Maçâ", "Goaiaba", "Acerola"]
vazia = []
letras = list("Academia")
numeros = list(range(20))
carro = ["RAM", "RAMPAGE R/T", 2025, "Esportivo", "R$ 274.990", 20]


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

for fruta in frutas:
    print(fruta)

for index, fruta in enumerate(frutas):
    print(f"index:{index} fruta:{fruta}")

pares = [numero for numero in numeros if numero % 2 == 0]

print(pares)
