class Account:
    def __init__(self, number, money=0):
        self.number = number
        self.money = money
    
    #Funktion för att hämta kontonummer
    def get_numbers(self):
        return self.number
    
    #Funktion för att hämta pengar
    def get_money(self):
        return self.money
    
    #Funktion för att lägga till pengar till kontot
    def deposit(self, money):
        self.money += money
        return self.money
    
    #Funktion för att hämta ut pengar från kontot
    def withdraw(self, money):
        self.money -= money
        return self.money

class Customer:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.accounts = []
    
    #Funktion för att hämta alla konto
    def get_accounts(self):
        return self.accounts
    
    #Funktion för att lägga till ett konto
    def add_account(self, number):
        self.accounts.append(Account(number))

class Bank:
    def __init__(self):
        self.customers = []
        self.current_customer = None
    
    #Funktion för att hämta alla kunder
    def get_customers(self):
        for customer in self.customers:
            print(customer.name, customer.password)
        return self.customers
    
    #Funktion för att lägga till kund
    def add_customer(self, customer):
        self.customers.append(customer)
    
    #Funktion för att hämta en specifik kund
    def get_customer(self, name):
        for customer in self.customers:
            if customer.name == name:
                print(f"Name: {customer.name}, Password: {customer.password}")
                return customer
        return None
    
    #Funktion för att ändra en kunds lösenord
    def change_customer_password(self, name, new_password):
        for customer in self.customers:
            if customer.name == name:
                customer.password = new_password
                return True
        return False
    
    #Funktion för att ta bort en kund
    def remove_customer(self, name):
        for customer in self.customers:
            if customer.name == name:
                self.customers.remove(customer)
                return True
        return False
    
    #Funktion för att logga in
    def login(self, username, password):
        for customer in self.customers:
            if customer.name == username and customer.password == password:
                self.current_customer = customer
                return True
        #Om man försöker logga in med en ny kund och skriver in fel användarnamn eller lösenord 
        self.current_customer = None                     #så loggas gamla kunden ut automatiskt
        return False
    
    #Funktion för att logga ut
    def logout(self):
        self.current_customer = None
    
    #Funktion för att hämta alla kontona för den inloggade kunden
    def get_accounts(self):
        if self.current_customer:
            for account in self.current_customer.get_accounts():
                print(f"Kontonummer: {account.get_numbers()}, Pengar: {account.get_money()}" )
            return self.current_customer.get_accounts()
    
    #Funktion för att lägga till konto för den inloggade kunden
    def add_account(self, number):
        if self.current_customer:
            self.current_customer.add_account(number)
    
    #Funktion för att ta bort ett konto för den inloggade kunden
    def remove_account(self, number):
        #x = 0
        for account in self.current_customer.get_accounts():
            if account.get_numbers() == number:
                self.current_customer.get_accounts().remove(account)
                return True
            #x +=1
        return False
    
    #Funktion för att få ett specifikt konto från den inloggade kunden
    def get_account(self, number):
        if self.current_customer:
            for account in self.current_customer.get_accounts():
                x = account.get_numbers()
                if x == number:
                    print(f"Kontonummer: {account.get_numbers()}, Pengar: {account.get_money()}kr")
                    return account
            return None
    
    #Funktion för att lägga till pengar till ett specifikt konto från den inloggade kunden
    def deposit(self, number, money):
        if self.current_customer:
            for account in self.current_customer.get_accounts():
                if account.get_numbers() == number:
                    print(f"Kontonummer: {account.get_numbers()}, Pengar: {account.get_money()}kr")
                    account.deposit(money)
                    print(f"Kontonummer: {account.get_numbers()}, Pengar: {account.get_money()}kr")
                    return True
            return False
    
    #Funktion för att lägga ta ut pengar från ett specifikt konto om man har pengarna från den inloggade kunden
    def withdraw(self, number, money):
        if self.current_customer:
            for account in self.current_customer.get_accounts():
                if account.get_numbers() == number:
                    if account.money >= money: 
                        print(f"Kontonummer: {account.get_numbers()}, Pengar: {account.get_money()}kr")
                        account.withdraw(money)
                        print(f"Kontonummer: {account.get_numbers()}, Pengar: {account.get_money()}kr")
                        return True
                    else:
                        print("You don't have enough money")
            return False
    
    #Funktion för att kunna se om någon är inloggad och isådanna fall vem som är det
    def print_current_customer(self):
        if self.current_customer != None:
            print(f"Logged in user is {self.current_customer.name} with password {self.current_customer.password}")
        else:
            print("No one is logged in")