#Oluwaseun as the group leader started with the import command,  variables, for loop,greetings, Open Account & Transfer
import random

# Initialize an empty string to store the account number
user_account = ""

# Generate a random account number
for _ in range(10):  # Generate 10 digits for the account number
    digit = random.randint(0, 9)  # Generate a random digit between 0 and 9
    user_account += str(digit)  # Append the digit to the account number
print("Welcome to Wema Bank Plc. \nHow maywe help you today?")
print("1. Open account\n2. Transfer\n3. Airtime\n4. Internet\n5. Balance\n6. Bills & Utitilies")
response = str(input( )).lower()
if response == "1" or response == "open account": 
    firstname = str(input("Your firstname\n>> ")).upper()
    surname = str(input("Your lastname\n>> ")).upper()
    other_name = str(input("Your other name\n>> ")).upper()
    gender = str(input("Your Gender\n>> ")).upper()
    email = str(input("Your email\n>> ")).upper()
    number = int(input("Your Phone number\n>> "))
    address = (input("your address\n>> ")).upper()
    dob = input("Your date of birth (MM/DD/YYYY)\n>> ")
    print("\nThank you for filling out the form.")
    print("Your account has been created successfully.")
    print("Here is your account information:")
    print(f"Name: {firstname} {other_name} {surname}")
    print(f"Date of Birth: {dob}")
    print("Address:", address)
    print("Account Number:", user_account)
    print("Thank you for choosing our bank")
elif response == "2" or response == "transfer":
    print("Choose the bank you are Transfering to: /n1. GT Bank ")
else:
    print("Invalid command")


