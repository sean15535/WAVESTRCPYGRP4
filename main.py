#Oluwaseun as the group leader started with the import command,  variables, for loop,greetings, Open Account & Transfer
# This program simulates a basic banking system for Wema Bank Plc.
# It generates a random 10-digit account number for new accounts and offers options for account opening, transfers,
# airtime purchases, internet banking, balance inquiries, and bill payments.
# Goodness worked on airtime and data, continue and logout, using variables, while loop etc. 
# Emmanuel worked utilities and check balance
from functions import username_login, phone_number_login, email_login, create_account, transfer
print("WELCOME TO WEMA MOBILE APP")
print("1. Login already existing account \n2. Open New Account/Sign Up")
choose = int(input())
if choose == 1:
    print("\nLogin with: \n1. Username \n2. Phone number \n3. email")
    reply = int(input())
    if reply == 1:
        username_login()
    elif reply == 2:
        phone_number_login()
    elif reply == 3:
        email_login()
    else:
        print("Invalid Response!")
elif  choose == 2: 
     create_account()
else:
    print("Invalid Request!")
print("Dashboard \n What would you like to do? \n1. Transfer \n2. Buy Airtime \n3. Buy Data \n4. Check Balance \n5. Utilities")
option = int(input())
if option == 1:
   transfer()
elif option == 2:
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
elif option == 3:
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
elif option == 4:
    p=4
    pin = int(input("Enter Transfer pin: "))
    while pin != p:
        print(f"{names}, your Account Balance is.....")
        break
    else:
        print("Incorrect pin")
        try_again = int(input("Enter Transfer pin: "))
elif option == 5:
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
print("Do you want to continue or logout?")
print("1. Continue \n2. Logout")
res = int(input("Option:"))
if res==1:
    print("Dashboard \n What would you like to do? \n1. Buy Airtime \n2. Buy Data \n3. Check Balance \n4. Utilities")
    option = int(input())
    if option == 1:
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
    elif option == 2:
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
    elif option == 3:
        p=4
        pin = int(input("Enter Transfer pin: "))
        while pin != p:
            print(f"{names}, your Account Balance is.....")
            break
        else:
            print("Incorrect pin")
            try_again = int(input("Enter Transfer pin: "))
    elif option == 4:
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
elif res==2:
        print("You have logged out successfully, goodbye!")
else:
        print("Invalid Response!")










    
            


        