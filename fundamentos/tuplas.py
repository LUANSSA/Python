print("Tuplas se parecem com Listas mas são CONSTANTES não podem ser modificadas")
amigos = ("Luan", "Álvaro", "Isadora", "Paulo")
print(amigos)

print("\nPosso usar os itens da tupla mas não posso modificar a tupla")
print("\n".join(amigos))

print("\nTamanho da tupla")
print(len(amigos))

print("\nEtiquetando tupla de amigos")
amigo1, amigo2, amigo3, amigo4 = amigos
print(amigo1)
print(amigo2)
print(amigo3)
print(amigo4)

print("\nCriando uma tupla x que contém os números 1 2 3 4")
x = (1,2,3,4)
print(x)

print("\nConvertendo tupla em lista usando o list()")
numeros = list(x)
print(numeros)