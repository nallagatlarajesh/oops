#encapsulation example code
#in this we seen private ,protected ,and public attributes
class bankaccount:
    def __init__(self,account_number,balance):
        self.account_number=account_number
        self._balance=balance   #private attribute
        
    def getbalance(self):
        return self._balance
    
    def deposite(self,amount):
        self._balance+=amount

#creating object ( instance )of the  bank account
account=bankaccount("12345",1000)
#accessing a private attribute using a methode
print(account.getbalance())

#modifying a private attribute
account.deposite(500)
print(account.getbalance())
