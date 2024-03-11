import random
balance = 50000
def username_login():
    response = str(input("Username: ")).capitalize()
    click = str(input("Password: ")).lower()
    print(f"Your login was successful, {response}")

def generate_account_number():
     number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
     result = ""
     for _ in range(10):  # Generate 10 digits for the account number
        digit = random.randint(0, 9)  # Generate a random digit between 0 and 9
        result += str(digit) 
     return result

def phone_number_login():
    response = int(input("Phone Number: "))
    num = 11
    while response!=num:
        click = str(input("Password: ")).lower()
        print(f"Your login was successful, {response}")
        break

def email_login():
    email = "@gmail.com"
    response = str(input(" ")).capitalize()
    print(f"{response}{email}")
    click = str(input("Password: ")).lower()
    print(f"Your login was successful, {response}")

def create_account():
    first_name = str(input("First name: ")).capitalize()
    last_name = str(input("Last name: ")).capitalize()
    other_names = str(input("Other names: ")).capitalize()
    names = first_name + last_name + other_names
    date_of_birth=input("Date of birth? \n Follow the format: day/month/year \n")
    home_address=input("Home Address: ")
    ph_num = int(input("Phone Number: "))
    length = 11
    while len(ph_num) != lenght or not ph_num.isdigit():
        print("Invalid Phone number!")
        ph_num = int(input("ph_num: "))
    sex=int(input("Sex: \n1. Male \n2. Female \n"))
    if sex==1 or 2:
        marital_status=int(input("Marital Status: \n1. Single \n2. Married \n "))
        if marital_status==1 or 2:
            email = str(input("Email: "))
            username = str(input("Username:"))
            password = input("Password: ")
            confirm_password = input("Confirm Password: ")
            while password != confirm_password:
                print("Passwords do not match!")
                password = input("Password: ")
                confirm_password = input("Confirm Password: ")

            print("\nThank you for filling out the form.")
            print("Your account has been created successfully.")
            print("Here is your account information:")
            print(f"Date of Birth: {date_of_birth}")
            print(f"Address: {home_address}")
            print(f"Phone number: {ph_num}") 
            print(f"\nYour Login was Successful! \nWelcome, {names} \n Your account number is {generate_account_number()}")                                                       
    
                    
        else:
            print("Error")
    else:
        print("Invalid Command!")        


def transfer():
    print("Choose the bank you are Transfering to: \n1. GT Bank \n2. Eco Bank \n3. Access Bank \n4. Wema Bank \n5. United Bank For Africa \n6. Other Options ")
    reply = input(">> ").lower()
    if reply == "1" or reply == "gtb" or reply == "gt bank" or reply == "gtbank":
        # Transfer to GT Bank
        recipient_account_number = int(input("Enter the recipient's GT Bank account number: "))
        num=10
        while recipient_account_number!=num:
                            amount = int(input("Enter the amount you want to transfer: "))

                            # Placeholder for transfer process
                            print(f"Transferring ₦{amount} to GT Bank account number {recipient_account_number}...")
                            print("Transfer successful! \nThnaks for banking with us😉")
                            break
        else:
            print("Invalid!")
    elif reply == "2" or reply == "eco bank" or reply == "eco":
        # Transfer to Eco Bank
        recipient_account_number = int(input("Enter the recipient's Eco Bank account number: "))
        num=10
        while recipient_account_number!=num:
                        amount = int(input("Enter the amount you want to transfer: "))

                        # Placeholder for transfer process
                        print(f"Transferring ₦{amount} to Eco Bank account number {recipient_account_number}...")
                        print("Transfer successful! \nThanks for banking with us😉")
                        break
        else:
            print("Invalid!")
    elif reply == "3" or reply == "access bank" or reply == "access" :
        # Transfer to Access Bank
        recipient_account_number = int(input("Enter the recipient's Access Bank account number: "))
        num=10
        while recipient_account_number!=num:
                        amount = int(input("Enter the amount you want to transfer: "))

                        # Placeholder for transfer process
                        print(f"Transferring ₦{amount} to Access Bank account number {recipient_account_number}...")
                        print("Transfer successful! \nThanks for banking with us😉")
                        break
        else:
             print("Invalid!")
    elif reply == "4" or reply == "wema" or reply == "wema bank":
        # Transfer to Wema Bank
        recipient_account_number = int(input("Enter the recipient's Wema Bank account number: "))
        num=10
        while recipient_account_number!=num:
                        amount = int(input("Enter the amount you want to transfer: "))

                        # Placeholder for transfer process
                        print(f"Transferring ₦{amount} to Wema Bank account number {recipient_account_number}...")
                        print("Transfer successful! \nThanks for banking with us😉")
                        break
        else:
             print("Invalid!")
    elif reply == "5" or reply == "uba" or reply == "united bank for africa":
        # Transfer to United Bank For Africa
        recipient_account_number = int(input("Enter the recipient's United Bank For Africa account number: "))
        num=10
        while recipient_account_number!=num:
                        amount = int(input("Enter the amount you want to transfer: "))

                        # Placeholder for transfer process
                        print(f"Transferring ₦{amount} to United Bank For Africa account number {recipient_account_number}...")
                        print("Transfer successful! \nThanks for banking with us😉")
                        break
        else:
             print("Invalid!")
    elif reply == "6" or reply == "other transfer options":
        # Other transfer options (placeholder)
        print("Choose Other transfer options:\n7. First Bank \n8. Globus Bank \n9.Opay \n10.Palmpay")
        choice = input(">> ").lower()
        if choice == "7" or reply == "first bank":
            # Transfer to First Bank
                recipient_account_number = int(input("Enter the recipient's First Bank account number: "))
                num=10
                while recipient_account_number!=num:
                                amount = int(input("Enter the amount you want to transfer: "))

                                # Placeholder for transfer process
                                print(f"Transferring ₦{amount} to First Bank  account number {recipient_account_number}...")
                                print("Transfer successful! \nThanks for banking with us😉")
                                break
                else:
                     print("Invalid!")
        elif choice == "8" or reply == "globus bank":
            # Transfer to Globus Bank
                recipient_account_number = int(input("Enter the recipient's Globus Bank account number: "))
                num=10
                while recipient_account_number!=num:
                                amount = int(input("Enter the amount you want to transfer: "))

                                # Placeholder for transfer process
                                print(f"Transferring ₦{amount} to Globus Bank  account number {recipient_account_number}...")
                                print("Transfer successful! \nThanks for banking with us😉")
                                break
                else:
                     print("Invalid!")
        elif choice == "9" or reply == "opay":
            # Transfer to OPAY
                recipient_account_number = int(input("Enter the recipient's OPAY account number: "))
                num=10
                while recipient_account_number!=num:
                                amount = int(input("Enter the amount you want to transfer: "))

                                # Placeholder for transfer process
                                print(f"Transferring ₦{amount} to OPAY  account number {recipient_account_number}...")
                                print("Transfer successful! \nThanks for banking with us😉")
                                break
                else:
                     print("Invalid!")
        elif choice == "10" or reply == "palmpay":
            # Transfer to Palmpay
                recipient_account_number = int(input("Enter the recipient's Palmpay account number: "))
                num=10
                while recipient_account_number!=num:
                                amount = int(input("Enter the amount you want to transfer: "))

                                # Placeholder for transfer process
                                print(f"Transferring ₦{amount} to Palmpay account number {recipient_account_number}...")
                                print("Transfer successful! \nThanks for banking with us😉")
                                break
                else:
                     print("Invalid!")
        else:
                print("invalid bank choice")
    else:
        print("Invalid bank choice")

def buy_airtime():
    print("1. MTN \n2. Glo \n3. 9mobile")
    pick = int(input("Option: "))
    if pick == 1:
        phone_number = int(input("Phone number: "))
        limit = 11
        while phone_number != limit:
            amount=int(input("Amount:# "))
            print(f"Your have successfully bought #{amount} airtime")
            break
    elif pick==2:
        phone_number = int(input("Phone number: "))
        limit = 11
        while phone_number != limit:
            amount=int(input("Amount: # "))
            print(f"Your have successfully bought #{amount} airtime")
            break
    elif pick==3:
        phone_number = int(input("Phone number: "))
        limit = 11
        while phone_number != limit:
            amount=int(input("Amount: # "))
            print(f"Your have successfully bought #{amount} airtime")
            break
    else:
        print("Invalid Request")

def buy_data():
    print("1. MTN \n2. Glo \n3. 9mobile")
    pick = int(input("Option: "))
    if pick == 1:
        phone_number = int(input("Phone number: "))
        limit = 11
        while phone_number != limit:
            option_1=("100MB")
            option_2=("200MB")
            option_3=("2.5MB")
            option_4=("1GB")
            option_5=("12GB")
            print("a. 100MB (1 Day @ #100) \nb. 200MB (3 Days @ #200) \nc. 2.5GB (2 Days @ #600) \nd. 1GB (7 Days @ #600) \ne. 12GB (30 Days @ #4000)")
            click = str(input("Option: "))
            if click=="a":
                print(f"Your have successfully purchased{ option_1} data.")
            elif click=="b":
                print(f"Your have successfully purchased{ option_2} data.")
            elif click=="c":
                print(f"Your have successfully purchased{ option_3} data.")
            elif click=="d":
                print(f"Your have successfully purchased{ option_4} data.")
            elif click=="e":
                print(f"Your have successfully purchased{ option_5} data.")
            else:
                print("Invalid Command")
            break
    elif pick==2:
        phone_number = int(input("Phone number: "))
        limit = 11
        while phone_number != limit:
            option_1=("50MB")
            option_2=("350MB")
            option_3=("1.8GB")
            option_4=("7GB")
            option_5=("9.2GB")
            print("a. 50MB (1 Day @ #50) \nb. 350MB (2 Days @ #200) \nc. 1.8GB (14 Days @ #500) \nd. 7GB (7 Days @ #1500) \ne. 9.2GB (30 Days @ #2000)")
            click = str(input("Option: "))
            if click=="a":
                print(f"Your have successfully purchased {option_1} data.")
            elif click=="b":
                print(f"Your have successfully purchased {option_2} data.")
            elif click=="c":
                print(f"Your have successfully purchased {option_3} data.")
            elif click=="d":
                print(f"Your have successfully purchased {option_4} data.")
            elif click=="e":
                print(f"Your have successfully purchased {option_5} data.")
            else:
                print("Invalid Command")
            break
    elif pick==3:
        phone_number = int(input("Phone number: "))
        limit=11
        while phone_number != limit:
            option_1=("100MB")
            option_2=("650MB")
            option_3=("1GB")
            option_4=("7GB")
            option_5=("6.2GB")
            print("a. 100MB (1 Day @ #100) \nb. 650MB (1 Day @ #200) \nc. 1GB (1 Day @ #600) \nd. 7GB (7 Days @ #1500) \ne. 6.2GB (30 Days @ #1200)")
            click = str(input("Option: "))
            if click=="a":
                print(f"Your have successfully purchased {option_1} data.")
            elif click=="b":
                print(f"Your have successfully purchased {option_2} data.")
            elif click=="c":
                print(f"Your have successfully purchased {option_3} data.")
            elif click=="d":
                print(f"Your have successfully purchased {option_4} data.")
            elif click=="e":
                print(f"Your have successfully purchased {option_5} data.")
            else:
                print("Invalid Command")
            break
    else:
        print("Invalid Request")

def account_balance():
    p=4
    pin = int(input("Enter Transfer pin: "))
    while pin != p:
        print(f" your Account Balance is ${balance}")
        break
    else:
        print("Incorrect pin")

def utilities():
    print("1. Pay Electricity bill \n2. Subscribe DSTV \n3. Other Billers")
    ruj = int(input("Select option: "))
    if ruj == 1:
        cardnumber = int(input("Bill code: "))
        bill=11
        while cardnumber!=bill:
            howmuch=int(input("Amount:#"))
            print(f"Your #{howmuch} subscription was successful!")
            break
        else:
            print("Invalid number")
    elif ruj == 2:
        code = int(input("Bill code: "))
        bill=11
        while code!=bill:
            howmuch=int(input("Amount:#"))
            print(f"Your #{howmuch} subscription was successful!")
            break
        else:
            print("Invalid number")
    elif ruj == 3:
        biller_name=str(input("Biller name:")).capitalize()
        billcode = int(input("Bill code: "))
        bill=11
        while billcode!=bill:
            howmuch=int(input("Amount:#"))
            print(f"Your #{howmuch} subscription from {biller_name} was successful!")
            break
        else:
            print("Invalid number")
    else:
        print("Invalid Request!")

def dashboard():
    print("Dashboard \n What would you like to do? \n1. Transfer \n2. Buy Airtime \n3. Buy Data \n4. Check Balance \n5. Utilities")
    option = int(input())
    if option == 1:
        transfer()
    elif option == 2:
        buy_airtime()
    elif option == 3:
        buy_data()
    elif option == 4:
        account_balance()
    elif option == 5:
        utilities()
    return



