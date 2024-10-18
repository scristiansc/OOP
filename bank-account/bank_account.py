# Definición de la clase
class BankAccount:
    # Definición del método constructor.
    # `self` representa las instancias* de la clase, no la clase como tal
    # * las instancias en las que se llaman los datos o functions
    def __init__(self, account_number, balance, owner):
        self.account_number = account_number
        self.balance = balance
        self.owner = owner

    # Definición de comportamiento:

    # Método o función retirar
    def withdraw(self, amount):
        self.balance = self.balance - amount

    # Método o función depositar
    def deposit(self, amount):
        self.balance = self.balance + amount

    # Método o función transferir*
    # * A repasar
    def transfer(self, other_account, amount):
        other_account.deposit(amount)
        self.withdraw(amount)