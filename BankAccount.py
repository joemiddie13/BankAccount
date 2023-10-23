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
  
  def withdraw(self, amount):
    if amount > self.balance:
      print("Insufficient funds. You will be charged an overdraft fee of $10.00.")
      self.balance -= 10
    else:
      self.balance -= amount
      print(f"Amount withdrawn: ${amount:.2f} = New Balance: ${self.balance:.2f}")
  
  def get_balance(self):
    print(f"Hello! Your current account balance is: ${self.balance:.2f}.")
    return self.balance
  
  def add_interest(self):
    interest = []
    annual_interest = 0.00083
    interest = self.balance * annual_interest
    return interest

rocko_bank = BankAccount("Rocko Paul")

print(f"Initial balance: ${rocko_bank.balance:.2f}")

rocko_bank.deposit(1000)
print(f"After deposit: {rocko_bank.balance:.2f}")

rocko_bank.withdraw(500)
print(f"After withdraw: {rocko_bank.balance:.2f}")

rocko_bank.get_balance()

rocko_bank.add_interest()
rocko_bank.get_balance()