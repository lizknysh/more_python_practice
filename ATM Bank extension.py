# Welcome introduction
print("Welcome to the Intergalactic Bank ATM! 🌌")
name = input("Please insert your card.... (Enter your name): ")
print()
print(f"Welcome to the Intergalactic Bank ATM, {name}")
print()

# Predefined PIN login for the user
pin = "4173"
attempts = 0
logged_in = False

# 3 maximum attempts to input the correct PIN number
for attempts in range(3):
    user_pin = input("Please enter your PIN: ")
    if user_pin == pin:
        print("Login accepted!")
        logged_in = True
        break
    else:
        print("Incorrect PIN! Try again, carefully.")
        remaining = 2 - attempts
        if remaining > 0:
            print(remaining, "attempts left.")
# If 3 attempts reached and failed
if logged_in == False:
    print("Blocked! Maximum attempts reached. Calling the police now...☎️")

# Show ATM menu after successful login
else:
    balance = 1000.00  # Starting balance for the user

    # Transaction history
    transaction_history = []
    # Direct Deposit 
    direct_deposit = []

# Direct deposit for loop for information input
    def direct_deposit_info():
        while True:
            bank = input("Enter your bank (CIBC, RBC, BMO): ")
            if bank == "CIBC" or bank == "RBC" or bank == "BMO":
                break
            else:
                print("ERROR: Unsupported bank. Only CIBC, RBC or BMO is supported.")

        while True:
            account_number = input("Enter your 8-digit account number: ")
            if len(account_number) == 8 and account_number.isdigit(): # Separate the error messages **
                break
            else:
                print("ERROR: Account number must be exactly 8 digits.")

        while True:
            transit_number = input("Enter your 3-digit transit number: ")
            if len(transit_number) == 3 and transit_number.isdigit():
                break
            else:
                print("ERROR: Transit number must be 3 digits only.")
        return [bank, account_number, transit_number]

# Main ATM menu loop
    while True:
        print("------------------------------")
        print("What would you like to do today?")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. View Transaction History")
        print("5. Direct Deposit")
        print("6. Exit")
        print("------------------------------")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            amount = float(input("Enter the amount to deposit: $"))

            if amount < 0:
                print("You can't deposit a negative amount! Transaction canceled. ❌")
            else:
                balance = balance + amount
                transaction_history.append("+$" + str(int(amount)))
                print("Deposit successful! 💰")
                print(f"${amount:.2f} has been deposited. New balance: ${balance:.2f}")

        elif choice == '2':
            amount = float(input("Enter the amount to withdraw: $"))
            if amount < 0:
                print("You can't withdraw a negative amount! Transaction canceled. ❌")
            elif amount > balance:
                print("Insufficient funds! Transaction canceled. ❌")
            else:
                balance = balance - amount
                transaction_history.append("-$" + str(int(amount)))
                print("Withdrawal successful! 💵")
                print(f"${amount:.2f} has been withdrawn. New balance: ${balance:.2f}")

        elif choice == '3':
            print(f"Your current balance is: ${balance:.2f}")

        elif choice == '4':
            print("Transaction History:")
            if len(transaction_history) == 0:
                print("No transactions yet.")
            else:
                for transaction in transaction_history:
                    print(transaction)

        elif choice == '5':
            if direct_deposit:
                print("Direct Deposit Information is already saved.")
                print("Bank:", direct_deposit[0])
                print("Account Number:", direct_deposit[1])
                print("Transit Number:", direct_deposit[2])
            else:
                direct_deposit = direct_deposit_info()
                print("Direct Deposit Information has been saved.")

        elif choice == '6':
            print()
            print("Thank you for using the Intergalactic Bank ATM! 🌌")
            print("Have a great day,", name + "!")
            break
        else:
            print("Invalid choice! Please select a number from 1 to 6.")

        print()  # Print a blank line for better readability