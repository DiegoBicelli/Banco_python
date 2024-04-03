#Variaveis
saldo = 0
rodar = True
numero_saques = 0
LIMITE = 500
LIMITE_SAQUES = 3
extratos = ""
menu = """"
=========BANCO COMUNISTA===========
[1] Extrato
[2] Deposito
[3] Saque
[4] Sair
"""
#Funções
def depositar():
    global extratos
    global saldo
    valor = input("Digite o valor do deposito: ")
    valor = float(valor)
    saldo += valor
    extratos += f" Deposito: R$: {valor:.2f}\n "
def sacar():
    global saldo
    global LIMITE_SAQUES
    global numero_saques
    global LIMITE
    global extratos

    valor = input("Digite o valor do saque: ")
    valor = float(valor)
    if numero_saques <= LIMITE_SAQUES:
        if valor <= LIMITE:
            if valor <= saldo:
                saldo -= valor
                extratos += f"Saque: R$: {valor:.2f}\n "
            else:
                print("Você não tem esse valor na conta!")
        else:
            print("Voce não pode sacar um valor maior que o limite de 500 reais!")
        numero_saques += 1
    else:
        print("Voce não pode sacar mais hoje!")
def extrato():
    global saldo
    global extratos
    titulo = "EXTRATO"
    print(titulo.center(30,"-"))
    if extratos is "":
        print("Nada no extrato")
    else:
        print(extratos)
        print(f"Saldo total:{saldo:.2f} ")
def escolha():
    escolha_valida = False
    while escolha_valida != True:
        escolha = input("Selecione uma operação: ")
        if escolha is "1":
            escolha_valida = True
            extrato()
        elif escolha is "2":
            escolha_valida = True
            depositar()
        elif escolha is "3":
            escolha_valida = True
            sacar()
        elif escolha is "4":
            global rodar
            escolha_valida = True
            rodar = False
        else:
            print("Escolha invalida tente novamente")
            escolha_invalida = False

# Main
while rodar == True:
    print(menu)
    escolha()
