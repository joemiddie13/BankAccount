# Import (random) method to assist in generating random account numbers
import random

# Create BankAccount class
class BankAccount:
  def __init__(self, full_name, account_number=None, account_type="savings"):
    self.full_name = full_name
    if account_number:
      self.account_number = account_number
    else:
      self.account_number = self.generate_account_number()
    self.balance = 0
    self.account_type = account_type # Stretch challenge (1/4)
  
  def generate_account_number(self):
    """Generates a random 8-digit account number."""
    return random.randint(10000000, 99999999)
  
  def deposit(self, amount):
    """Deposits a given amount of $ to the bank account."""
    self.balance += amount
    print(f"Amount deposited: ${amount:.2f} = New Balance: ${self.balance:.2f}")
  
  def withdraw(self, amount):
    """Withdraws a specified amount of $ from the bank account."""
    if amount > self.balance:
      print("Insufficient funds. You will be charged an overdraft fee of $10.00.")
      self.balance -= 10
    else:
      self.balance -= amount
      print(f"Amount withdrawn: ${amount:.2f} = New Balance: ${self.balance:.2f}")
  
  def get_balance(self):
    """Simple statement printing to the terminal of the current balance."""
    print(f"Hello! Your current account balance is: ${self.balance:.2f}.")
    return self.balance
  
  def add_interest(self):
    """Adds a monthly interest based on a 0.083% interest rate."""
    if self.account_type == "savings":
      annual_interest = 0.012
    else:
      annual_interest = 0.00083
    interest = self.balance * annual_interest
    self.balance += interest

  def print_statement(self):
    """Prints a nicely formatted bank account statement."""
    formatted_balance = "{:,.2f}".format(self.balance)
    print(f"""
          {self.full_name}
          Account Type: {self.account_type.capitalize()}
          Account No.: {self.account_number}
          Balance: ${formatted_balance}
          """)

#########################################################################    

# (5) Rocko BankAccount Example (1/3)

# Instantiate Rocko's bank account information
rocko_bank = BankAccount("Rocko Paul", "savings")

# Display Rocko's bank account information
rocko_bank.print_statement()

# Rocko get's a huge allowance from his dad, Joe Paul
rocko_bank.deposit(130000)
print("Rocko! Woof! You got a nice allowance from Dad!")

# Rocko immediately buys the entire Costco stock of dental sticks
rocko_bank.withdraw(1000)

# Display Rocko's new bank account balance
rocko_bank.print_statement()

#########################################################################

# (5) Dad deposits money and gets some interest Example (2/3)

# Instantiate Dad's bank account information
dad_bank = BankAccount("Dad Paul")

# Display Dad's bank account information
dad_bank.print_statement()

# Dad comes home from work, back in the day, and deposits his work check
dad_bank.deposit(2000)

# It is the end of the month so let's reward Dad with some interest
dad_bank.add_interest()

# Let's check out the updated balance!
dad_bank.print_statement()

#########################################################################

# (5) Mango gets an allowance, but doesn't have enough for a hair cut

# Instantiate Mango's bank account information
mango_bank = BankAccount("Mango Tango")

# Display Mango's bank account information
mango_bank.print_statement()

# Deposit an allowance into Mango's bank
mango_bank.deposit(100)

# Mango needs a hair cut BAD
mango_bank.withdraw(150)

# Poor Mango needs more money
mango_bank.deposit(500)

# Gets a nice hair cut!
mango_bank.withdraw(150)

# Display Mango's final account balance for the day
mango_bank.print_statement()

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

#########################################################################
# Stretch challenge (2/4)

bank = []
bank.append(rocko_bank)
bank.append(dad_bank)
bank.append(mango_bank)
bank.append(mitchell_bank)

def add_interest_accounts():
  """Loop applies interest to all accounts within the bank list."""
  for account in bank:
    account.add_interest()

add_interest_accounts()

rocko_bank.print_statement()
dad_bank.print_statement()
mango_bank.print_statement()
mitchell_bank.print_statement()