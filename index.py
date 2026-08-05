def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")
def deposit(balance):
    amount = float(input("Enter an amount to be deposited: "))
    if amount < 0 :
        print("That is not a valid amount")
        return 0
    else : 
        return amount
def withdraw(balance):
    amount = float(input("Enter the amount you would like to deposit: "))
    if amount > balance :
        print("Insufficient balance")
        return 0
    elif amount < 0 :
        print("amount should be greater than zero")
        return 0

    else:
         return amount
    

def main():
    balance = 0
    is_running = True
    while is_running:
        print("Banking Program")
        print("1.Show balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        choice = input("Enter your choice to (1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance = balance + deposit(balance)
        elif choice == '3':
            balance = balance - withdraw(balance)
        elif choice == '4':
            is_running = False
        else :
            print("That is not a valid choice")

if __name__ == "__main__":
    main()
print("Thank you! have a good day ")