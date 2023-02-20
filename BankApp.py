#Importing the classes and functions
import BankAppClass as ba

#Renaming the classes to easier variables
bank = ba.Bank()
customer = ba.Customer("", "")

#Importing so i can clear the terminal
from os import system, name

#Function so i can clear the terminal
def clear():
    if name == 'nt':
        _ = system('cls')

#Function for the main menu
def MainMenu():
    #Looping so the menu stays up until canceled or changing menu
    while(True):
        #Clearing to make it cleaner
        clear()
        
        #Printing the choices
        print("1. Login:")
        print("2. Create a Customer Account:")
        print("3. Exit")

        #Getting a choice from the user
        userChoice = int(input("Choose your option: "))

        #Whaterver choice the user picks gets a new menu or exits the program
        if userChoice == 1:
            #If the user chooses to log in
            LoggedIn()
        elif userChoice == 2:
            #If the user chooses to create an account
            CreateCustomer()
        elif userChoice == 3:
            #If the user wants to exit the program
            break
        else:
            #If the user chooses an invalid choice the error text comes up
            print("Please enter a valid number")

#Function for creating a customer
def CreateCustomer():
    #Clearing to make it cleaner
    clear()

    #Getting the username and password from the user
    username = input("What do you want your username to be: ")
    password = input("What do you want your password to be: ")

    #Using a function from the bank class to add the customer
    bank.add_customer(ba.Customer(username, password))

#Function for logging in
def LoggedIn():
    #Clearing to make it cleaner
    clear()

    #Creating a global variable to use it else where
    global loginUsername

    #Getting the username and password from the user to log in
    loginUsername = input("Username: ")
    password = input("Password: ")

    #Getting all the customers that are created
    for customers in bank.customers:
        #If the inputed username and password matches an existing customer username and password
        if loginUsername == customers.name and password == customers.password:
            #Using a function from the bank class to login
            bank.login(loginUsername, password)

            #Using the menu for when the user is logged in
            LoggedInMenu()
        #If the inputed username or password doesn't match it will print a error text
        else:
            #Clearing to make it cleaner
            clear()

            #Print error text
            print("Wrong Username Or Password")
            input("Press Enter To Return:")
        
#Function for the menu when the user is logged in
def LoggedInMenu():
    #Looping so the menu stays up until canceled or changing menu
    while(True):
        #Clearing to make it cleaner
        clear()

        #Printing the choices
        print("1. Get all accounts: ")
        print("2. Get an account: ")
        print("3. Add an account: ")
        print("4. Change password: ")
        print("5. Logout")

        #Getting a choice from the user
        userChoice = int(input("Choose your option: "))

        #Whaterver choice the user picks gets a new menu or exits the program
        if userChoice == 1:
            clear()
            #Prints all the accounts the customer has
            bank.get_accounts()

            #Staying so the user can see all the accounts
            input("Press Enter To Return:")
        elif userChoice == 2:
            clear()
            #Prints all the accounts the customer has so the user can choose
            bank.get_accounts()

            #Getting a choice from the user
            accountChoice = input("Choose an account: ")

            #Getting the specific account the user chose
            ChoosenAccount(accountChoice)
        elif userChoice == 3:
            clear()
            #Getting a choice from the user
            number = input("Account Number: ")

            #Using a function from the bank class to add an account
            bank.add_account(number)
        elif userChoice == 4:
            clear()
            #Getting a choice from the user
            passwordChoice = input("Choose your new password: ")

            #Using a function from the bank class to choose a new password
            bank.change_customer_password(loginUsername ,passwordChoice)
        elif userChoice == 5:
            #The logged in customer gets logged out
            bank.logout()

            #Returns to the main menu
            break
        else:
            #If the user chooses an invalid choice the error text comes up
            print("Please enter a valid number")

#Function for the menu of the chosen account
def ChoosenAccount(number):
    #Looping so the menu stays up until canceled or changing menu
    while(True):
        #Clearing to make it cleaner
        clear()

        #Printing out the account number and money
        bank.get_account(number)

        #Printing the choices
        print("1. Deposit: ")
        print("2. Withdraw: ")
        print("3. Remove account: ")
        print("4. Go back: ")

        #Getting a choice from the user
        userChoice = int(input("Choose your option: "))

        #Whaterver choice the user picks gets a new menu or exits the program
        if userChoice == 1:
            clear()
            #Getting the amount of money to deposit into the account
            depositMoney = int(input("How much money do you want to deposit: "))

            #Using a function from the bank class to deposit money into the chosen account
            bank.deposit(number, depositMoney)
        elif userChoice == 2:
            clear()
            #Getting the amount of money to withdraw from the account
            withdrawMoney = int(input("How much money do you want to withdraw: "))

            #Using a function from the bank class to withdraw money from the chosen account
            bank.withdraw(number, withdrawMoney)
        elif userChoice == 3:
            #Using a function from the bank class to remove the chosen account
            bank.remove_account(number)

            #Returns to the logged in menu
            break
        elif userChoice == 4:
            #Returns to the logged in menu
            break
        else:
            #If the user chooses an invalid choice the error text comes up
            print("Please enter a valid number")

#Starting the program
MainMenu()