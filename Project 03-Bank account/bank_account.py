accounts = {}

#create account
def create_account():
    acc_no = input("Enter Account Number: ")

    if acc_no in accounts:
        print("Account already exists.")
        return

    name = input("Enter Account Holder Name: ")
    balance = float(input("Enter Initial Deposit: "))

    accounts[acc_no] = {
        "name": name,
        "balance": balance,
        "transactions": ["Account created with Rs. " + str(balance)]
    }

    print("Account created successfully!")


# Deposit Money
def deposit_money():
    acc_no = input("Enter Account Number: ")

    if acc_no in accounts:
        amount = float(input("Enter amount to deposit: "))

        if amount > 0:
            accounts[acc_no]["balance"] += amount

            accounts[acc_no]["transactions"].append(
                "Deposited Rs. " + str(amount)
            )

            print("Money deposited successfully!")
        else:
            print("Enter a valid amount.")

    else:
        print("Account not found.")


# Withdraw Money
def withdraw_money():
    acc_no = input("Enter Account Number: ")

    if acc_no in accounts:
        amount = float(input("Enter amount to withdraw: "))

        if amount <= 0:
            print("Enter a valid amount.")

        elif amount > accounts[acc_no]["balance"]:
            print("Insufficient balance.")

        else:
            accounts[acc_no]["balance"] -= amount

            accounts[acc_no]["transactions"].append(
                "Withdrawn Rs. " + str(amount)
            )

            print("Money withdrawn successfully!")

    else:
        print("Account not found.")


# Check Balance
def check_balance():
    acc_no = input("Enter Account Number: ")

    if acc_no in accounts:
        print("Account Holder:", accounts[acc_no]["name"])
        print("Current Balance: Rs.", accounts[acc_no]["balance"])
    else:
        print("Account not found.")


# Display Transaction History
def transaction_history():
    acc_no = input("Enter Account Number: ")

    if acc_no in accounts:
        print("\n--- Transaction History ---")

        for transaction in accounts[acc_no]["transactions"]:
            print(transaction)

    else:
        print("Account not found.")


# Save Data
def save_data():
    file = open("bank_data.txt", "w")

    for acc_no in accounts:
        account = accounts[acc_no]

        file.write("Account Number: " + acc_no + "\n")
        file.write("Account Holder: " + account["name"] + "\n")
        file.write("Balance: " + str(account["balance"]) + "\n")

        file.write("Transaction History:\n")

        for transaction in account["transactions"]:
            file.write(transaction + "\n")

        file.write("-------------------------\n")

    file.close()

    print("Bank data saved successfully!")


# Main Program
while True:

    print("\n===== BANK ACCOUNT MANAGEMENT SYSTEM =====")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Transaction History")
    print("6. Save Data")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        create_account()

    elif choice == 2:
        deposit_money()

    elif choice == 3:
        withdraw_money()

    elif choice == 4:
        check_balance()

    elif choice == 5:
        transaction_history()

    elif choice == 6:
        save_data()

    elif choice == 7:
        print("Thank you for using the Bank Management System!")
        break

    else:
        print("Invalid choice. Please try again.")
