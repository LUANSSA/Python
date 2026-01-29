# Conjuntos
conjuntoNomes = set()
print(conjuntoNomes)

# Adicionando item nos conjuntos
conjuntoNomes.add("Luan")
conjuntoNomes.add("Marcela")
conjuntoNomes.add("Caio")

print("\nNão se repete itens em conjuntos")
conjuntoNomes.add("Luan")
conjuntoNomes.add("Luan")
print(conjuntoNomes)

print("\nObserve que não se repete")
conjuntoTeste = set({"Caio", "Lucas", "Caio", "Luan"})
print(conjuntoTeste)

print("\nUsando a função remove() para remover o item 'Lucas'")
conjuntoTeste.remove("Lucas")
print(conjuntoTeste)

print("\nConjunto de números")
conjuntoNumeros = set({1,2,3,4,5})
print(conjuntoNumeros)
conjuntoNumeros.add(6)
conjuntoNumeros.add(7)

print("\nRemove do inicio até o final em vez do final até o inicio como em listas")
conjuntoNumeros.pop()
conjuntoNumeros.pop()
print(conjuntoNumeros)
