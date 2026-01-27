# 📚 Explicação Completa do Código de Listas em Python

Este documento explica **cada função, método e comando** utilizado no código fornecido, com foco didático para quem está aprendendo Python.

---

## 🖨️ Função `print()`

```python
print("texto")
```

* Exibe informações no terminal.
* `\n` cria uma nova linha antes do texto.
* `*` é apenas um caractere visual para separação.

---

## 📦 Criação de Listas

```python
frutas = ["Laranja", "Banana", "Maçã", "Goiaba", "Acerola"]
```

* Lista com valores do tipo `string`.

```python
vazia = []
```

* Lista vazia.

```python
letras = list("Academia")
```

* Converte a string em uma lista de caracteres.

```python
numeros = list(range(20))
```

* `range(20)` gera números de 0 a 19.
* `list()` converte para lista.

```python
carro = ["RAM", "RAMPAGE R/T", 2025, "Esportivo", "R$ 274.990", 20]
```

* Lista com **tipos mistos** (string e int).

---

## 🔎 Acessando e Fatiando Listas (Slicing)

```python
lista = list("Academia")
```

### 📌 Exemplos

```python
lista[::-1]
```

* Inverte a lista.

```python
lista[2:]
```

* Do índice 2 até o final.

```python
lista[:2]
```

* Do início até o índice 1.

```python
lista[1:4]
```

* Do índice 1 ao 3.

```python
lista[0:8:2]
```

* Percorre pulando de 2 em 2.

```python
len(lista)
```

* Retorna o tamanho da lista.

---

## 🔁 Laços de Repetição com Listas

```python
for fruta in frutas:
```

* Percorre cada item da lista.

```python
for index, fruta in enumerate(frutas):
```

* `enumerate()` retorna índice + valor.

---

## 🧠 List Comprehension

```python
pares = [numero for numero in numeros if numero % 2 == 0]
```

* Cria uma nova lista.
* Filtra apenas números pares.

---

## 📑 Cópia de Lista

```python
listaCopia = lista.copy()
```

* Cria uma **cópia independente** da lista.

```python
listaCopia.append("Y")
```

* Adiciona item ao final.

---

## 🔢 Contagem e Busca

```python
lista.count("a")
```

* Conta quantas vezes o item aparece.

```python
lista.index("A")
```

* Retorna o índice da primeira ocorrência.

---

## 🔗 Junção de Listas

```python
lista.extend(listaCopia)
```

* Junta duas listas.

---

## 🧹 Remoção de Itens

```python
listaCopia.pop()
```

* Remove o último item.

```python
listaCopia.pop(0)
```

* Remove pelo índice.

```python
lista.remove("a")
```

* Remove a **primeira ocorrência** do valor.

---

## 🔄 Inversão de Lista

```python
lista.reverse()
```

* Inverte a lista no próprio objeto.

---

## 🔠 Ordenação de Listas

```python
linguagens.sort()
```

* Ordenação crescente.

```python
linguagens.sort(reverse=True)
```

* Ordenação decrescente.

---

## ⚙️ Ordenação com Função Anônima (lambda)

```python
linguagens.sort(key=lambda x: len(x))
```

* Ordena pelo tamanho da string.

```python
linguagens.sort(key=lambda x: len(x), reverse=True)
```

* Do maior para o menor.

---

## 🧩 Função Built-in `sorted()`

```python
sorted(linguagens)
```

* Retorna nova lista ordenada.
* Não altera a original.

---

## 🧱 Lista de Listas (Matriz)

```python
listaAmigos = [["Luan", "Salvador", "BA", 27]]
```

* Cada item é uma lista.

```python
listaAmigos.append([...])
```

* Insere nova lista.

```python
listaAmigos.pop(0)
```

* Remove lista pelo índice.

```python
listaAmigos[0].pop(1)
```

* Remove item da lista interna.

```python
listaAmigos.insert(1, [...])
```

* Insere lista em posição específica.

---

## 📌 Acesso por Índice Negativo

```python
listaAmigos[-1]
```

* Último item.

```python
listaAmigos[-1][-1]
```

* Último elemento da última lista.

---

## ✅ Conclusão

Este código demonstra **praticamente tudo que você precisa saber sobre listas em Python**:

* Criação
* Acesso
* Fatiamento
* Loops
* Cópia
* Ordenação
* Listas aninhadas

Perfeito como material de estudo ou referência 📘🐍
