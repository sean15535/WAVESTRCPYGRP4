def username_login():
    response = str(input("Username: ")).capitalize()
    click = str(input("Password: ")).lower()
    print(f"Your login was successful, {response}")
def phone_number_login():
    response = int(input("Phone Number: "))
    num = 11
    while response!=num:
        click = str(input("Password: ")).lower()
        print(f"Your login was successful, {response}")
        break