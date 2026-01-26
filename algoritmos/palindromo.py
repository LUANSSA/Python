# Biblioteca de string
import string

# Verifica se é palindromo
def palindromo(frase):
    
    # Pontuações
    excluirPontuacao = set(string.punctuation)

    # Frase sem pontuação
    fraseLimpa = "".join(letra for letra in frase if letra not in excluirPontuacao)
    # Frase sem espaços em branco
    fraseLimpa = fraseLimpa.replace(" ", "")
    # Frase em minúsculo
    fraseLimpa = fraseLimpa.lower()

    # Verifica se é palindromo (igual de trás para frente)
    if fraseLimpa == fraseLimpa[::-1]:
        return True
    else:
        return False

def main():

    while True:
        frase = input("Digite uma frase: ")
        
        if(palindromo(frase)):
            print(f"A frase '{frase}' é um palindromo!")
        else:
            print(f"A frase '{frase}' não é um palindromo!")

    
if __name__ == "__main__":
    main()
    