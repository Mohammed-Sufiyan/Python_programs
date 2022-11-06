# This project is about creating a ATM Machine
# This is very simple and easy, using classes, objects, if-else, try-except concepts are used.....
# This project is for beginners who want to imporve their learning skills through python, this is for them!

import random
import sys

class ATM():
    def __init__(self, name, account_number, balance = 0):
        self.name = name
        self.account_number = account_number
        self.balance = balance
    def account_details(self):
        print("\n----------ACCOUNT DETAILS----------")
        print(f"Account Holder : {self.name.upper()}")
        print(f"Account Number : {self.account_number}")
        print(f"Account Balance : Nu.{self.balance}\n")
    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Current account balance : Nu.", self.balance)
        print()
    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance - self.amount:
            print("Insufficient Fund!")
            print(f"Your balance is Nu.{self.balance} only.")
            print("Try with lesser amount balance : Nu.", self.balance)
            print()
        else:
            self.balance = self.balance - self.amount
            print(f"Nu. {amount} withdrawal successful!")
            print("Current account balance : Nu.", self.balance)
            print()
    def check_balance(self):
        print("Available Balance : Nu.",self.balance)
        print()
    def transaction(self):
        print("""
            TRANSACTION
          **********************
            Menu : 
            1. Account Details
            2. Check Balance
            3. Deposit
            4. Withdraw
            5. Exit
           *********************** """)
        while True:
            try:
                option = int(input("Enter 1, 2, 3, 4 or 5 : "))
            except:
                print("Error : Enter 1, 2, 3, 4 or 5 only!\n")
                continue
            else:
                if option == 1:
                    atm.account_details()
                elif option == 2:
                    atm.check_balance()
                elif option == 3:
                    amount = int(input("How much you want to deposit(Nu.) : "))
                    atm.deposit(amount)
                elif option == 4:
                    amount = int(input("How much you want to withdraw(Nu.) : "))
                    atm.withdraw(amount)
                elif option == 5:
                    print(f"""
                            Printing Receipt
                    *******************************************
                        Transaction is now complete.
                        Transaction number : {random.randint(10000, 1000000)}
                        Account holder : {self.name.upper()}
                        Account Number : {self.account_number}
                        Available Balance : Nu.{self.balance}
                        Thanks for Choosing us as your bank 
                    ********************************************""")
                    sys.exit()
print("********WELCOME TO BANK OF BIRMINGHAM********")
print("-------------------------------------------")
print("---------TO OPEN A NEW BANKING ACCOUNT--------")
name = input("Enter your name:- ")
account_number = input("Enter your account number:- ")
print("Congratulations!  Your Account has been created Successfully!.....\n")

atm = ATM(name, account_number)
while True:
    trans = input("Do you want to do any transaction?1 for yes/ 0 for no  : ")
    if trans == "1":
        atm.transaction()
    elif trans == "0":
        print("""
         -------------------------------------------
        |   Thanks for Choosing us as your bank     |
        |   Visit us again!                         |
         ------------------------------------------""")
        break
    else:
        print("Wrong command! Enter 'y' for yes and 'n' for No.\n")
