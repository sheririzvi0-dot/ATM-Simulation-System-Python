class User:
    def __init__(self, name, pin, balance):
        self.name = name
        self.pin = pin
        self.balance = balance 
        self.history = []   #transaction history list
    def add_history(self, action):
        self.history.append(action)
    def check_balance(self):
        print(f"💰 Your current balance is: {self.name}, your balance is: {self.balance}")
        self.add_history(f"Checked balance")
    def deposit(self, amount):
        if amount <= 0:
            print("❌ Invalid deposit amount. Please enter a positive value.")
            return
        self.balance += amount
        print(f"✅ Successfully deposited {amount}. New balance: {self.balance}")
        self.add_history(f"Deposited {amount}")
    def withdraw(self, amount):
        if amount <= 0:
            print("❌ Invalid withdrawal amount. Please enter a positive value.")
        elif amount > self.balance:
            print("❌ Insufficient funds. Withdrawal failed.")
        else:
            self.balance -=amount
            print(f"✅ Successfully withdrew {amount}. New balance: {self.balance}")
            self.add_history(f"Withdrew {amount}")
    def show_history(self):
        print("📜 Transaction History:")
        if not self.history:
            print("No transactions yet.")
        else:
            for i,h in enumerate(self.history, 1):
                print(f"{i}. {h}")

class ATMSystem:
    def __init__(self):
        self.users={}   #Sample users (you can add more)
        self.users["Harrey"]= User("Harrey", "1234", 50000)
        self.users["John"]= User("John", "5678", 78000)
    def login(self):
        print("========= Welcome to the ATM System! 🏦💳=========")
        name=input("Enter your name: ")
        if name not in self.users:
            print("❌ User not found. Please check your name.")
            return None
        user=self.users[name]
        attempts= 3
        while attempts > 0:
            pin=input("Enter your PIN:")
            if pin==user.pin:
                print(f"✅ Login successful! Welcome {user.name}.")
                return user
            else:
                attempts -=1
                print(f"❌ Incorrect PIN. You have {attempts} attempts left.")
                print(" Account Locked.")
                return None
    def run(self):
        user=self.login()
        if not user:
            return
        while True:
            print("\n========= ATM Menu =========")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Show Transaction History")
            print("5. Logout")
            print("==============================")
            choice=input("Select an option (1-5): ")
            if choice=="1":
                user.check_balance()
            elif choice=="2":
                amount=float(input("Enter the amount to deposit: "))
                user.deposit(amount)
            elif choice=="3":
                amount=float(input("Enter the amount to withdraw: "))
                user.withdraw(amount)
            elif choice=="4":
                user.show_history()
            elif choice=="5":
                print(f"👋 Goodbye {user.name}! Thank you for using the ATM System.")
                break
            else:
                print("❌ Invalid option. Please select a valid option (1-5).")

# Run the ATM system

if __name__=="__main__":
    atm=ATMSystem()
    atm.run()