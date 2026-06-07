# **************** Simple ATM Machine ************************
def main(): # Main function
    atm_pin = 1992
    balance = 10000
    
    while True:  # Loop used to automate the repeatition of the program for better service.
        try:    # try-except statement used to handle mismatch errors.
            print("-"*25)
            print("Welcome to XYZ Bank (ATM)")
            print("-"*25)
            atm_pass = int(input(f"\nPlease enter you ATM pin or type 0 to exit: "))

            if atm_pass == atm_pin: # Used conditional statement to dictate multiple path of code.
                print("Welcome!\n")

                print("-"*39)
                choice = int(input("What action you would like to perfrom?\n"
                    "1. Cash Withdrawl\n"
                    "2. Cash Deposit\n"
                    "3. Balance Check\n"
                    "4. Exit\n"
                    "Press (1, 2, 3, 4) in respect to your need: "))
                print("-"*45)

                match choice:   # Another Conditional Statement used for similar purpose
                    case 1:
                        Withdraw_money = int(input("Enter the amount to money you want to Withdraw: "))
                        
                        if Withdraw_money <= 0:
                            print("Please enter a valid ammount.")

                        
                        elif Withdraw_money <= balance:
                            print("Successfuly Done!")
                            balance -= Withdraw_money
                            print(f"Your new balance is: {balance}")
                            print("-"*39)

                        else:
                            print(f"You don't have enough money.\n"
                                f"Current balance: {balance}")
                            print("-"*39)

                    case 2:
                        print("-"*39)
                        deposit_money = int(input("Enter the amount to money you want to Deposit: "))
                        
                        if deposit_money < 0: 
                            print("This action is unacceptible.")
                        else:
                            balance += deposit_money
                            print(f"Successfuly Done!\n"
                                f"Current balance {balance}")
                        print("-"*39)

                    case 3: 
                        print("-"*29)
                        print(f"You'r current balance is: {balance}")
                        print("-"*29)

                    case 4:
                        print("-"*29)
                        print("Thanks for using ATM. Have a great time.")
                        print("-"*29)
                        break

                    case _:
                        print("-"*39)
                        print('Please choose an option or exit using the option 4.')
                        print("-"*39)
                        continue
            
            elif atm_pass == 0:
                print("Bye")
                break
            else:
                print("\nIncorrect Pin. Try again.")
                continue

            print("-"*39)
            ask = input("Do you want to perform another transaction? (Y/n): ").lower()
            if ask == 'n':  # Condition to check whether the user wants to continue or not.
                print("Thanks for using.")
                print("-"*39)
                break
            else:
                continue
        except ValueError: 
            print("Enter a correct value to further a do.")
            continue

if __name__ == "__main__":
    main()