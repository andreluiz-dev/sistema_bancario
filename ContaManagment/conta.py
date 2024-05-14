class ContaBancaria():
    def __init__(self, titular: str, saldo: float, limite: float) -> None:
        self.titular = titular
        self.limite = limite
        self.saldo = saldo
        
    def depositar(self, valor: float) -> None:
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")
    
    def sacar(self, valor: float) -> None:
        if valor > self.saldo:
            print("Operação falhou! Saldo insuficiente.")
        
        elif valor > self.saldo and valor > self.limite:
            print("Operação Falhou! Valor do saque excedeu o limite.")
        
        elif valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        
        elif valor > 0 and valor <= self.limite:
            self.saldo -= valor
            self.limite -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        
        else:
            print("Operação falhou! Valor inválido.")
            
    def extrato(self) -> None:
        print("\n ######## EXTRATO ########")
        print(f"Titular: {self.titular}")
        print(f"Saldo: R$ {self.saldo:.2f}")
        print(f"Limite: R$ {self.limite:.2f}")
        print("#################################")