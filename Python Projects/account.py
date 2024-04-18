from bank_account import BankAccount

account1 = BankAccount(23030)
account2 = BankAccount(22202)
account3 = BankAccount(24630)

account1.deposit(1000)
print(account1)

account1.withdraw(250)
print(account1)

account2.withdraw(25)
print(account2)

print(account1.get_balance())

account4 = BankAccount(69696969696969696969696969696969696969696969696969696969)
account4.deposit(420420420420420420420420420)
print(account4)