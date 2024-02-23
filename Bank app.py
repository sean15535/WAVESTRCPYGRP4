#Oluwaseun as the group leader started with the greetings messages, variables, Open Account & Transfer
a =[0,1,2,3,4,5,6,7,8,9]
b =[9,8,7,6,5,4,3,2,1,0]
c =[0,1,2,3,4,5,6,7,8,9]
d =[9,8,7,6,5,4,3,2,1,0]
e =[0,1,2,3,4,5,6,7,8,9]
f =[9,8,7,6,5,4,3,2,1,0]
g =[0,1,2,3,4,5,6,7,8,9]
h =[9,8,7,6,5,4,3,2,1,0]
i =[0,1,2,3,4,5,6,7,8,9]
j =[9,8,7,6,5,4,3,2,1,0]

aa = a[9]
bb = b[0:10]
cc = c[2:9]
dd = d[3:8]
ee = e[-6:-1]
ff = f[6:9]
gg = g[4:9]
hh = h[5:9]
ii = i[6:9]
jj = j[1:7]

account_number = ''

for aa in a:
    for bb in b:
        for cc in c:
            for dd in d:
                for ee in e:
                    for ff in f:
                        for gg in g:
                            for hh in h:
                                for ii in i:
                                    for jj in j:
                                         account_number = str(aa) + str(bb) + str(cc) + str(dd) + str(ee) + str(ff) + str(gg) + str(hh) + str(ii) + str(jj)  
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
    print(f"Dear {firstname} {surname} {other_name}, your account was successfully created,\nyour account number is {account_number}\nThank you for choosing our bank")
elif response == "2" or response == "transfer":
    print("Choose the bank you are Transfering to: ")
else:
    print("Invalid command")


