#Oluwaseun as the group leader started with the import command,  variables, for loop,greetings, Open Account & Transfer
# This program simulates a basic banking system for Wema Bank Plc.
# It generates a random 10-digit account number for new accounts and offers options for account opening, transfers,
# airtime purchases, internet banking, balance inquiries, and bill payments.
# Goodness worked on airtime and data, continue and logout, using variables, while loop etc. 
# Emmanuel worked utilities and check balance
from functions import username_login, phone_number_login, email_login, create_account, transfer, buy_airtime, buy_data, account_balance, utilities, dashboard
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
dashboard()
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
print("Do you want to continue or logout?")
print("1. Continue \n2. Logout")
res = int(input("Option:"))
if res==1:
    dashboard()
elif res==2:
        print("You have logged out successfully, goodbye!")
else:
        print("Invalid Response!")
   