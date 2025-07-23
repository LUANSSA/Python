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


# Interpolação de variáveis em strings
nome = "Luan"
idade = 28
cidade = "Salvador"
estado = "Bahia"
# Old style %
print("Olá, %s! Você tem %i anos e mora em %s/%s." % (nome, idade, cidade, estado)) # Olá, Luan! Você tem 28 anos e mora em Salvador/Bahia.


print("********* ---------- **********")
# Saída dos exemplos a seguir: Olá, Luan! Você tem 28 anos e mora em Salvador/Bahia. Luan em Salvador temos vários cursos disponíveis para você.

# Método .format
print("Olá, {}! Você tem {} anos e mora em {}/{}. {} em {} temos vários cursos disponíveis para você.".format(nome, idade, cidade, estado, nome, cidade))
# Método .format com índice
print("Olá, {0}! Você tem {1} anos e mora em {2}/{3}. {0} em {2} temos vários cursos disponíveis para você.".format(nome, idade, cidade, estado))
# Método .format com nome de variável
print("Olá, {nome}! Você tem {idade} anos e mora em {cidade}/{estado}. {nome} em {cidade} temos vários cursos disponíveis para você.".format( nome = nome, idade = idade, cidade = cidade, estado = estado))
# Método f-string
print(f"Olá, {nome}! Você tem {idade} anos e mora em {cidade}/{estado}. {nome} em {cidade} temos vários cursos disponíveis para você.")

print("********* ---------- **********")
# Método f-string formantado a string
PI = 3.14159
print(f"Valor de PI: {PI}") # Valor de PI: 3.14159
print(f"Valor de PI: {PI:.2f}") # Valor de PI: 3.14
print(f"Valor de PI: {PI:10.2f}") # Valor de PI:       3.14

print("********* ---------- **********")
# Fatiamento de String
nome = "Luan Lima de Souza"
# Tamanho da String
print(f"O nome '{nome}' tem {len(nome)} caracteres.") # O nome 'Luan Lima de Souza' tem 18 caracteres.

print(nome[0]) # L
print(nome[-1])# a
print(nome[-2])# z
print(nome[:11]) # Luan Lima d
print(nome[11:]) # e Souza
print(nome[5:9]) # Lima
print(nome[0:18:2]) # La iad oz
print(nome[:]) # Luan Lima de Souza
print(nome[0:18]) # Luan Lima de Souza

# Espelhamento da string
print(nome[::-1]) # azuoS ed amiL nauL

# String múltiplas linhas
print(f"""
========== MENU ==========
      
    1 - Cadastrar
    2 - Listar
    3 - Perfil
    4 - Configurações
    5 - Sair      

==========      ==========
""")



