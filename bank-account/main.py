from bank_account import BankAccount

# Creación de instancias/objetos
cuenta_de_cristian = BankAccount("1234567", 50_000,"cristian")
cuenta_del_fil = BankAccount("007564", 10_000,"Fil")

# Acceso a los datos de un objeto
# Para ello, utilizamos the dot syntax
print(f"El número de cuenta de Cristian es: {cuenta_de_cristian.account_number}")
print(f"El saldo de la cuenta de Cristian es: {cuenta_de_cristian.balance}")

print("---------------------------------\n")

# Acceso al comportamiento / métodos de un objeto
# Para ello, utilizamos the dot syntax as well
print("Withdrawing money from Cristian's account...")
cuenta_de_cristian.withdraw(10_000)
# Volvemos a imprimir
print(f"El nuevo saldo de la cuenta del Cristian es: {cuenta_de_cristian.balance}")
print(f"El Fil tiene: {cuenta_del_fil.balance}")

# Depositamos en la cuenta del Fil
print("---------------------------------\n")
print("Depositing money on Fil's account...")
cuenta_del_fil.deposit(40_000)

# Imprimimos el estado de las cuentas
print("---------------------------------\n")
print(f"El Fil tiene ahora: {cuenta_del_fil.balance}")
print(f"El Cristian tiene ahora: {cuenta_de_cristian.balance}")

# Transferimos del Fil al Cristian
print("---------------------------------\n")
print("Transfiriendo 2000 de Fil a Cristian")
cuenta_del_fil.transfer(cuenta_de_cristian, 2_000)

# Imprimimos el estado final de las cuentas
print("---------------------------------\n")
print(f"El Fil tiene ahora: {cuenta_del_fil.balance}")
print(f"El Cristian tiene ahora: {cuenta_de_cristian.balance}")
