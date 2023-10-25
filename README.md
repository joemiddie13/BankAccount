# Student Information
Joseph Paul
October 25, 2023
ACS 1111 Object Oriented Programming

# Assignment
Project Title: Bank Account
Programming Language: Python
Code Editor: VS Code

Our class is learning object oriented programming for the first time and this is our first project. We were tasked with creating a class that defines a bank account to include some attributes you would expect: name, account number, and money balance.

At the start of my code you will find `import random` from the Python library allowing my program to randomize numbers which I utilized in account number creation.

Within the class attributes, I set `account_number=None` so that an account number could be randomized when a bank account was instantiated.

As part of one of the "stretch goals" I set the `account_type="savings"` so that the bank accounts could be defined.

As you scroll through the `BankAccount` class, you will find 6 methods that are common amongst real bank accounts. Ranging from depositing money, withdrawing money, and printing a current statement of your balance. 

Towards the bottom of `BankAccount.py` you will find 4 different bank account examples as asked by the requirements of the project.

To see the original assignment description assigned in class, please continue to scroll below:


ORIGINAL: Assignment Description from class:

# Bank Account 🏦

## Description

Using object-oriented programming concepts, your task is to create a Python program that simulates a bank account.

## Requirements

### Assignment Requirements:

Your job is to create a Class that defines a bank account. It should define the owners name, account number, and balance as attributes. 

Your BankAccount class should also define methods that perform common banking activities like deposit, withdraw, and get statement.

Follow the steps below: 

1. Your Python program should be created in one file called `BankAccount.py`.
1. Define a `BankAccount` class.
1. A bank account should have the following attributes:
   * `full_name` - the full name of the bank account account owner.
   * `account_number` - randomly generated 8 digit number, unique per account.
   * `balance` - the balance of money in the account, should start at 0.
4. Then define the following methods for the `BankAccount` class:
   * The `deposit` method will take one parameter `amount` and will **add** `amount` to the `balance`. Also, it will print the message: `“Amount deposited: $X.XX new balance: $Y.YY”`
   * The `withdraw` method will take one parameter `amount` and will **subtract** `amount` from the `balance`. Also, it will print a message, like `“Amount withdrawn: $X.XX new balance: $Y.YY”`. If the user tries to withdraw an amount that is greater than the current balance, print `”Insufficient funds.”` and charge them with an overdraft fee of `$10`
   * The `get_balance` method will `print` a user-friendly message with the account balance and then also `return` the current `balance` of the account.
   * The `add_interest` method adds interest to the users `balance`. The annual interest rate is 1% (i.e. 0.083% per month). Thus, the monthly interest is calculated by the following equation: `interest = balance *  0.00083 `.
   * The `print_statement` method prints a message with the account name, account number, and balance like this:
   ```
   Joi Anderson
   Account No.: ****5678
   Balance: $100.00
   ```
5. Outside of the BankAccount class, define 3 different bank account examples using the `BankAccount()` object.
   * Your examples should show you using the different methods above to demonstrate them working.
6. Include example code to do the following: 
   - Create a new bank account instance: user: "Mitchell", account number: 03141592. 
   - Deposit $400,000 into "Mitchell's" account. 
   - Print a statement
   - Add interest to the account
   - Print a statement
   - Make a withdrawl of $150 (Mitchell needs some Yeezy's)
   - Print a statement

### Stretch Challenges (Optional)

1. Add an attribute to set the account type: checking or savings. 
   - A savings account gets 1.2% insterest (that's 1% per month)
   - Create a checking and a savings account
   - Add interest to each account
   - Print a statement for each account
2. Create a list called: bank. Add all of your accounts to bank. Write a function that loops over all accounts in the list and calls the `add_interst` method of each. 
3. Create an "application". Use a loop to prompt us for an action. Actions can be: 
   - Create account
      - Prompt for name, number, and balance.
   - Statement - prompts for the account number and prints the statement for that account. 
   - Deposit - prompts for account number and amount. Then makes a deposit.
   - Withdraw - prompts for account number and amount. Then makes a withdrawl
4. Create a Bank class. This class will store a list of BackAccounts. It should implement the following methods: 
   - create_account() - creates a new account. 
   - deposit() - deposits an amount into an account with an account number
   - withdraw() - removes an amount from an account with an account number
   - transfer() - withdraws an amount from an account with an account number and deposits the same amount to an account with another number. 
   - statement() - prints an statement for an account with an account number. 

## Rubric

Use this rubric to measure your the success with this project: [Bank Account Rubric](https://docs.google.com/document/d/157PjRQ4Sy55eas7w7eK-JT36lm0wpGebSXpWvGj-ccg/edit?usp=sharing)