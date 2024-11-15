class Bank:
    bankTotalMoney = 0  

    def __init__(self, initialAmount):
        Bank.bankTotalMoney += initialAmount

    @classmethod
    def deposit_bank(cls, amt):
        cls.bankTotalMoney += amt
        print(f"Bank total after deposit: {cls.bankTotalMoney}")

    @classmethod
    def withdraw_bank(cls, amt):
        if amt > cls.bankTotalMoney:
            print("Insufficient funds in the bank!")
            return False
        cls.bankTotalMoney -= amt
        print(f"Bank total after withdrawal: {cls.bankTotalMoney}")
        return True


class Account(Bank):
    def __init__(self, userInitialBalance, bankInitialAmount):
        super().__init__(bankInitialAmount)  
        self.userBankBalance = userInitialBalance

    def deposit_user(self, amt):
        self.userBankBalance += amt
        self.deposit_bank(amt)  
        print(f"User balance after deposit: {self.userBankBalance}")

    def withdraw_user(self, amt):
        if amt > self.userBankBalance:
            print("Insufficient funds in user account!")
            return
        if self.withdraw_bank(amt):  
            self.userBankBalance -= amt
            print(f"User balance after withdrawal: {self.userBankBalance}")



if __name__ == '__main__':
    
    totalBankAmount = 500

   
    user1 = Account(200, totalBankAmount)
    user1.deposit_user(100) 
    user1.withdraw_user(50)  

    print('User 1 balance:', user1.userBankBalance)
    print('Bank total money:', Bank.bankTotalMoney)

    print()

    
    user2 = Account(0, 0)
    user2.deposit_user(300)  
    user2.withdraw_user(100)  

    print('User 2 balance:', user2.userBankBalance)
    print('Bank total money:', Bank.bankTotalMoney)
