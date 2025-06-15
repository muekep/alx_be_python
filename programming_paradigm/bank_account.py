class BankAccount:
    def __init__(self, initial_balance: float =0.0):

        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.account_balance = initial_balance
    def get_balance(self) -> float:
        return self.account_balance
    def deposit( self, amount:float ):
        
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.account_balance += amount
        print(f"Deposited ${amount:.1f}.")
        self.display_balance()
    def withdraw(self,amount:float) -> bool:
        
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"Withdrew ${amount:.1f}.")
            self.display_balance()
            return True
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.1f}")
