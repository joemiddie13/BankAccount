import random

class BankAccount:
  def __init__(self, full_name,): #account_number, #balance):
    self.full_name = full_name
    self.account_number = self.generate_account_number()
    self.balance = 0
  
  def generate_account_number(self):
    return random.randint(10000000, 99999999)

rocko_bank = BankAccount("Rocko Paul")
print(rocko_bank.account_number)