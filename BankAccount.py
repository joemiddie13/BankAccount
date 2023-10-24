import random

class BankAccount:
  def __init__(self, full_name, account_number=None):
    self.full_name = full_name
    if account_number:
      self.account_number = account_number
    else:
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
    annual_interest = 0.00083
    interest = self.balance * annual_interest
    self.balance += interest

  def print_statement(self):
    formatted_balance = "{:,.2f}".format(self.balance)
    print(f"""
          {self.full_name}
          Account No.: {self.account_number}
          Balance: ${formatted_balance}
          """)

# (5) Rocko Example

# rocko_bank = BankAccount("Rocko Paul")

# print(f"Initial balance: ${rocko_bank.balance:.2f}")

# rocko_bank.deposit(1000)
# print(f"After deposit: {rocko_bank.balance:.2f}")

# rocko_bank.withdraw(500)
# print(f"After withdraw: {rocko_bank.balance:.2f}")

# rocko_bank.get_balance()

# rocko_bank.add_interest()
# rocko_bank.get_balance()

# rocko_bank.print_statement()

#########################################################################

# (6) Mitchell Example!

# Instantiate Mitchell's bank account information using BankAccount class
mitchell_bank = BankAccount("Mitchell Hudson", "03141592")

# Initialize a deposit of $400,000 to Mitchell's bank account
mitchell_bank.deposit(400000)

# Print Mitchell's bank account statement
mitchell_bank.print_statement()

# Add interest to Mitchell's bank account
mitchell_bank.add_interest()

# Print Mitchell's updated bank account statement after interest
mitchell_bank.print_statement()

# Withdraw $150 so Mitchell can fit some fresh new Nike's
mitchell_bank.withdraw(150)

# Print final statement of Mitchell's spending habit for the day
mitchell_bank.print_statement()