class Bankaccount:

    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance

    @property 
    def balance(self):
        return self.__balance
    
    #Deposit section
    def deposit(self,amount):

        if amount > 0 :
            self.__balance += amount
            print(f"{amount} is diposited ")
        else:
            print("Invalid amount")

    #Withraw section 
    def withraw(self,amount):

        if amount <= 0:
            print("Invalid amount")

        elif amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} of money is withrwed")
        else:
            print("Insufficient balance")
    #Account holder info
    def account_info(self):
        print(f"Account holder name is: {self.name}")
        print(f"Account Balance is: {self.__balance}")

account = Bankaccount("Rakib",10000)

#Account holder info
account.account_info()

#Deposit section
account.deposit(5000)

#Withraw section 
account.withraw(2000)

print("Final balance",account.balance)

    
