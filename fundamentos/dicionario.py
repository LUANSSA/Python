dicionario = {
    "nome": "Luan Souza",
    "idade": 27,
    "cidade": "Salvador",
    "estado": "Bahia"
}
print(
"""
| Método     | O que faz                    |
| ---------- | ---------------------------- |
| `keys()`   | retorna as chaves            |
| `values()` | retorna os valores           |
| `items()`  | retorna pares (chave, valor) |
| `update()` | junta ou atualiza            |
| `clear()`  | apaga tudo                   |
"""
)

print(f"Chaves: {dicionario.keys()}")
print(f"Valores: {dicionario.values()}")
print(f"Chaves e valores: {dicionario.items()}")


print(f"Tipo: {type(dicionario)}")

print("\nExibindo os itens do dicionário")
print(dicionario["nome"])
print(dicionario["idade"])
print(dicionario["cidade"])
print(dicionario["estado"])
# Exibindo os itens de forma segura
print(dicionario.get("email", "email não encontrado"))
print(dicionario.get("telefone", "telefone não encontrado"))

dicionario["idade"] = 28 # atualiza e não cria duplicata
dicionario["nome"] = "Luan Lima de Souza"
dicionario["email"] = "meuemail@gmail.com"

dicionario.update({
    "telefone": "71 90000-0000"
})

dicionario["alfabeto"] = "a", "b", "c", "d"

print("\nExibindo os itens do dicionário após modificações")
print(dicionario["nome"])
print(dicionario["idade"])
print(dicionario["cidade"])
print(dicionario["estado"])
print(dicionario["email"])
print(dicionario["telefone"])


dicionario[("a", "b", "c")] = True, False, True
dicionario[("d", "e", "f")] = [False, False, False]

print("\n********** Chaves do dicionário **********")
for chave in dicionario:
    print(chave)

print("\n********** Chaves e valores do dicionário **********")
for chave, valor in dicionario.items():
    print(f"{chave}: {valor}")

