
balance = 1000


def check_balance():
    return balance


def deposit():
    global balance

    try:
        amount = float(input("Enter deposit amount: "))

        if amount <= 0:
            return "Invalid deposit amount!", balance

        balance += amount
        return "Deposit successful!", balance

    except ValueError:
        return "Please enter a valid number!", balance


def withdraw():
    global balance

    try:
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            return "Invalid withdrawal amount!", balance

        elif amount > balance:
            return "Insufficient balance!", balance

        else:
            balance -= amount
            return "Withdrawal successful!", balance

    except ValueError:
        return "Please enter a valid number!", balance


while True:
    print("\n===== ATM BANKING SYSTEM =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Select a service (1-4): ")

    if choice == "1":
        current_balance = check_balance()
        print(f"Your current balance is: {current_balance:.2f} BDT")

    elif choice == "2":
        message, current_balance = deposit()
        print(message)
        print(f"Current balance: {current_balance:.2f} BDT")

    elif choice == "3":
        message, current_balance = withdraw()
        print(message)
        print(f"Current balance: {current_balance:.2f} BDT")

    elif choice == "4":
        print("Thank you for using our ATM!")
        break

    else:
        print("Invalid choice! Please select 1-4.")
