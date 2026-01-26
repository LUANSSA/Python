def trianguloRetangulo(a, b, c):
    tmp = c
    c = max(a, b, c)

    if(a == c):
        a = tmp
    elif(b == c):
        b = tmp

    if(a**2 + b**2 == c**2):
        return True
    
    return False


def main():
    while True:
        a = input("Digite o primeiro número do triângulo: ")
        b = input("Digite o segundo número do triângulo: ")
        c = input("DIgite o terceiro número do triângulo: ")

        if(trianguloRetangulo(int(a), int(b), int(c))):
            print("É um triângulo retângulo!")
        else:
            print("Não é um triângulo retângulo")

if __name__ == "__main__":
    main()