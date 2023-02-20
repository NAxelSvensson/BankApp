class Account:
    def __init__(self, number, money=0):
        self.number = number
        self.money = money
    
    #Function to get account numbers
    def get_numbers(self):
        return self.number
    
    #Function to get account money
    def get_money(self):
        return self.money
    
    #Function for depositing money to account
    def deposit(self, money):
        self.money += money
        return self.money
    
    #Function for withdrawing money from account
    def withdraw(self, money):
        self.money -= money
        return self.money

class Customer:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.accounts = []
    
    #Function to get all accounts
    def get_accounts(self):
        return self.accounts
    
    #Function to add an account
    def add_account(self, number):
        self.accounts.append(Account(number))

class Bank:
    def __init__(self):
        self.customers = []
        self.current_customer = None
    
    #Function to add a customer
    def add_customer(self, customer):
        self.customers.append(customer)
    
    #Function to change a customers password
    def change_customer_password(self, name, new_password):
        for customer in self.customers:
            if customer.name == name:
                customer.password = new_password
                return True
        return False
    
    #Function for logging in
    def login(self, username, password):
        for customer in self.customers:
            if customer.name == username and customer.password == password:
                self.current_customer = customer
                return True
        return False
    
    #Function for logging out
    def logout(self):
        self.current_customer = None
    
    #Function to get all accounts from the logged in customer
    def get_accounts(self):
        if self.current_customer:
            for account in self.current_customer.get_accounts():
                print(f"Kontonummer: {account.get_numbers()}, Pengar: {account.get_money()}" )
            return self.current_customer.get_accounts()
    
    #Function to add an account to the logged in customer
    def add_account(self, number):
        if self.current_customer:
            self.current_customer.add_account(number)
    
    #Function to remove an account from the logged in customer
    def remove_account(self, number):
        for account in self.current_customer.get_accounts():
            if account.get_numbers() == number:
                self.current_customer.get_accounts().remove(account)
                return True
        return False
    
    #Function to get a specific account from the logged in customer
    def get_account(self, number):
        if self.current_customer:
            for account in self.current_customer.get_accounts():
                x = account.get_numbers()
                if x == number:
                    print(f"Kontonummer: {account.get_numbers()}, Pengar: {account.get_money()}kr")
                    return account
            return None
    
    #Function for depositing money to an account from the logged in customer
    def deposit(self, number, money):
        if self.current_customer:
            for account in self.current_customer.get_accounts():
                if account.get_numbers() == number:
                    account.deposit(money)
                    return True
            return False
    
    #Function for withdrawing money from an account from the logged in customer
    def withdraw(self, number, money):
        if self.current_customer:
            for account in self.current_customer.get_accounts():
                if account.get_numbers() == number:
                    if account.money >= money: 
                        account.withdraw(money)
                        return True
            return False