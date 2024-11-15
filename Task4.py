# Parent class: Bank
class Bank:
    bankTotalMoney = 0  # Shared across all accounts

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


# Child class: Account
class Account(Bank):
    def __init__(self, userInitialBalance, bankInitialAmount):
        super().__init__(bankInitialAmount)  # Initialize the bank's total money
        self.userBankBalance = userInitialBalance

    def deposit_user(self, amt):
        self.userBankBalance += amt
        self.deposit_bank(amt)  # Deposit the same amount in the bank
        print(f"User balance after deposit: {self.userBankBalance}")

    def withdraw_user(self, amt):
        if amt > self.userBankBalance:
            print("Insufficient funds in user account!")
            return
        if self.withdraw_bank(amt):  # Check if the bank has enough money
            self.userBankBalance -= amt
            print(f"User balance after withdrawal: {self.userBankBalance}")


# Usage Example
if __name__ == '__main__':
    # Initialize the bank with 500 total money
    totalBankAmount = 500

    # User 1 opens an account with 200
    user1 = Account(200, totalBankAmount)
    user1.deposit_user(100)  # User deposits 100
    user1.withdraw_user(50)  # User withdraws 50

    print('User 1 balance:', user1.userBankBalance)
    print('Bank total money:', Bank.bankTotalMoney)

    print()

    # User 2 opens an account with 0
    user2 = Account(0, 0)
    user2.deposit_user(300)  # User deposits 300
    user2.withdraw_user(100)  # User withdraws 100

    print('User 2 balance:', user2.userBankBalance)
    print('Bank total money:', Bank.bankTotalMoney)
