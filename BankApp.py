import BankAppClass as ba
bank = ba.Bank()
customer = ba.Customer("", "")
from os import system, name

def clear():
    if name == 'nt':
        _ = system('cls')

def MainMenu():
    while(True):
        clear()
        print("1. Login:")
        print("2. Create a Customer Account:")
        print("3. Exit")
        userChoice = int(input("Choose your option: "))
        if userChoice == 1:
            LoggedIn()
        elif userChoice == 2:
            CreateCustomer()
        elif userChoice == 3:
            break
        else:
            print("Please enter a valid number")

def CreateCustomer():
    clear()
    username = input("What do you want your username to be: ")
    password = input("What do you want your password to be: ")
    bank.add_customer(ba.Customer(username, password))

def LoggedIn():
    clear()
    global loginUsername
    loginUsername = input("Username: ")
    password = input("Password: ")
    for customers in bank.customers:
        if loginUsername == customers.name and password == customers.password:
            bank.login(loginUsername, password)
            LoggedInMenu()
        else:
            print("Wrong Username Or Password")
            input("Press Enter To Return:")
        

def LoggedInMenu():
    while(True):
        clear()
        print("1. Get all accounts: ")
        print("2. Get an account: ")
        print("3. Add an account: ")
        print("4. Change password: ")
        print("5. Logout")
        userChoice = int(input("Choose your option: "))
        if userChoice == 1:
            clear()
            bank.get_accounts()
            input()
        elif userChoice == 2:
            clear()
            bank.get_accounts()
            accountChoice = input("Choose an account: ")
            ChoosenAccount(accountChoice)
        elif userChoice == 3:
            clear()
            number = input("Account Number: ")
            bank.add_account(number)
        elif userChoice == 4:
            clear()
            passwordChoice = input("Choose your new password: ")
            bank.change_customer_password(loginUsername ,passwordChoice)
        elif userChoice == 5:
            bank.logout()
            break
        else:
            print("Please enter a valid number")

def ChoosenAccount(number):
    while(True):
        clear()
        bank.get_account(number)
        print("1. Deposit: ")
        print("2. Withdraw: ")
        print("3. Remove account: ")
        print("4. Go back: ")
        userChoice = int(input("Choose your option: "))
        if userChoice == 1:
            clear()
            depositMoney = int(input("How much money do you want to deposit: "))
            bank.deposit(number, depositMoney)
        elif userChoice == 2:
            clear()
            withdrawMoney = int(input("How much money do you want to withdraw: "))
            bank.withdraw(number, withdrawMoney)
        elif userChoice == 3:
            bank.remove_account(number)
            break
        elif userChoice == 4:
            break
        else:
            print("Please enter a valid number")

MainMenu()
