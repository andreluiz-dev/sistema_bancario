menu = """

Selecione a opção da operação desejada:
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = menu

    if opcao == "1":
        valor = float(input("Digite o valor do depósito: "))

        if valor == 0: 
            saldo+=valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")
    
    elif opcao == "2":
        valor = float(input("Digite o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente.")
        
        elif excedeu_limite:
            print("Operação Falhou! Valor do saque excedeu o limite.")

        elif excedeu_saques:
            print("Operação Falhou! Limite de saques excedido.")

        elif valor > 0:
            saldo += valor
            extrato += f"Saque: R${valor:.2f}"
            numero_saques += 1
        
        else:
            print("Operação falhou! Valor inválido.")
    
    elif opcao == "3":
        print("\n ######## EXTRATO ########")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("#################################")

    elif opcao == "4":
        break

    else:
        print("Opção Inválida, por favor selecione novamente a operação desejada.")