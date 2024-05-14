import ContaManagment as cm

menu = ("""

Selecione a opção da operação desejada:
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

""")


if __name__ == "__main__":
    # Exemplo de uso da classe ContaBancaria
    conta = cm.ContaBancaria("Fulano", 1000, 500)
    while(1):
        opcao = input(menu)
        if opcao == "1":
            valor = float(input("Digite o valor do depósito: "))
            conta.depositar(valor)
        elif opcao == "2":
            valor = float(input("Digite o valor do saque: "))
            conta.sacar(valor)
        elif opcao == "3":
            conta.extrato()
        elif opcao == "4":
            break
        else:
            print("Opção Inválida, por favor selecione novamente a operação desejada.")