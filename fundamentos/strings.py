## Strings com PYTHON

# Variável
texto = "    Python "

print("Texto inicial:", texto) # "    Python "


print("********* ---------- **********")


# Maiúscula, Minúscula e Título
print("Texto usando ##.upper()## para deixar texto em maiúscolo:", texto.upper()) # "PYTHON"

print("Texto usando ##.lower()## para deixar o texto em minúsculo:", texto.lower()) # "python"

print("Texto usando ##.title()## para deixar o texto com primeira letra em maiúscula", texto.title()) # "Python"


print("********* ---------- **********")


# Eliminando espaços em branco
print("Texto usando ##.strip()## para remover espaços na esquerda e na direita:", texto.strip()) # "Python"

print("Texto usando ##.lstrip()## para remover espaços na direita:", texto.lstrip()) # "Python "

print("Texto usando ##.rstrip()## para remover espaços na esquerda:",texto.rstrip()) # "    Python"


print("********* ---------- **********")


# Junções e centralização
print("Texto usando ##.center(13, '#')## para centralizar e juntar caracteres", texto.center(13, "#")) # "#    Python #"

print("Texto usando ##'.'.join(texto)## para adicionar caractere entre os caracteres", ".".join(texto)) # " . . . .P.y.t.h.o.n. "



