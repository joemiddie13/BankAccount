import random

class BankAccount:
  def __init__(self, full_name,): #account_number, #balance):
    self.full_name = full_name
    self.account_number = self.generate_account_number()
    self.balance = 0
  
  def generate_account_number(self):
    return random.randint(10000000, 99999999)
  
  def deposit(self, amount):
    self.balance += amount
    print(f"Amount deposited: ${amount:.2f} = New Balance: ${self.balance:.2f}")

rocko_bank = BankAccount("Rocko Paul")

print(f"Initial balance: ${rocko_bank.balance:.2f}")

rocko_bank.deposit(500)
print(f"After deposit: {rocko_bank.balance:.2f}")