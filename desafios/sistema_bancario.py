# Variáveis e Constantes
opcao = 0
saldo = 0
extrato = []
LIMITE_SAQUE = 3

#  Menu de Opções
print(''' 
********** MENU **********
    
    1 - Depósito
    2 - Saque
    3 - Extrato
    4 - Sair
''')

#  Opção a ser selecionada
opcao = int(input("Escolha uma das opções acima (1, 2, 3, 4): "))


# Depósito
if opcao == 1:
    deposito = input("Digite o valor de depósito: ")

# Saque
elif opcao == 2:
    ...
# Extrato
elif opcao == 3:
    ...
# Finaliza
else:
    print("Operação FINALIZADA!")