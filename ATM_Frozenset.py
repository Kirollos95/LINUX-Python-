class ATM:
    def __init__(self):
        self.pin_numbers = frozenset(["1234", "5678", "9876"])  # Valid PIN numbers
        self.balance = 1000  # Initial balance

    def validate_pin(self, pin):
        if pin in self.pin_numbers:
            return True
        return False

    def check_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        self.balance -= amount
        return f"Withdrawal successful. Remaining balance: {self.balance}"

# Example usage:
atm = ATM()

pin = input("Enter your PIN: ")

if atm.validate_pin(pin):
    print("PIN validated")
    while True:
        print("1. Check Balance")
        print("2. Withdraw")
        print("3. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            balance = atm.check_balance()
            print(f"Your balance is: {balance}")
        elif choice == 2:
            amount = int(input("Enter the amount to withdraw: "))
            message = atm.withdraw(amount)
            print(message)
        elif choice == 3:
            print("Thank you for using the ATM!")
            break
        else:
            print("Invalid choice. Please try again.")
else:
    print("Invalid PIN")
