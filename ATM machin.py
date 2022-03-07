# d = {1:[1234,5000],2:[4321,10000],3:[1111,20000]}
# d["RR"] = 3456 # for new account
# d[3][0]=2222
# id = 9
# npin = 4545
# bal = 100000000
# d[id][0] = 1221
# d[id] = [npin,bal]
# print(d)
# print(d[1])
# print(d[1][0])
# bal = d[1][1]+1000
# print(bal)
# above is the teasting part for confermation



import sys
from os import system
from time import sleep

# FOLOWING ARE THE COSTOMER AND THEIR PINS
customer = {1:[1234,5000],2:[4321,10000],3:[1111,20000],4:[1212,1000]}

# FUCTION TO ADD NEW ACCOUNT
def add_acc(customer):
    # global customer
    n = int(input("Enter your new account ID: "))
    if n in customer:
        print("Your Account already Exist\nEnter unique ID")
    else:
        while True:
            npin = int(input("Enter Your New PIN"))
            npinc = int(input("Enter Your New PIN Again"))
            if npin==npinc:
                print("For Successful Ragistration\nDeposite Minimum Amount of '500Rs'")
                
                while True:
                    bal = int(input("Enter the Deposite Amount: "))
                    if bal>=500:
                        customer[n] = [npin,bal]
                        # customer[n][0] = npin
                        # customer[n][1] = bal
                        print("Your Acount is Successfully Opend.Your Balance is {}".format(bal))
                        break
                    else:
                        print("Deposite Minimum Amount of 500Rs")
                break

            else:
                print("PIN does not matched\nTry Again...")    
# Add Account fuctions Complited


# FUNCTION TO CHANGE THE PIN NUMBER
def change_pin(id):
    oldpin = int(input("Enter Your Old PIN: "))
    if oldpin == customer[id][0]:
        while True:
            pin = int(input("Enter Your New PIN: "))
            pinc = int(input("Enter Your New PIN Again: "))
            if pin==pinc:
                customer[id][0] = pin
                print("Your New PIN Updated")
                break
            else:
                print("PIN does not matched\nTry Again...")
    else:
        print("Enter Correct Old PIN")


# FUNCTION FOR ADMIN 
def admin():
    passw = 62323
    n = int(input("Enter 5 digit Admin Password: "))
    print(customer)


# MAIN FUNCTION 
while True:
    print()
    print("-------------------")
    print("Welcome to the ATM")
    print("-------------------")
    print()
    n = int(input("Press '1' to continue or '0' to exit: "))
    if n==1:
        id = int(input("Enter your card I.D.: "))
        if id in customer.keys():

            pin = int(input("Enter your 4 digit PIN : "))
            bal = customer[id][1]
            
            if customer[id][0]==pin:
                while True:
                    sleep(1)
                    # system('cls')
                    
                    print('''
    Enter...

    1. Deposite             4. Change PIN

    2. Withdrow             5. Add Account
    
    3. Bank Balance         6. Change ID    
    
    100. Admin              0. Exit
    
  
            ''')

                    uc = int(input("Enter your Choice here ->  "))
                    if uc==1:
                        #Function for amount deposited
                        ad = int(input("Enter the amount that you want to deposite: "))
                        bal = bal + ad
                        print("Your Amount = %.2f is successfully deposited.\nYour updated Amount is %.2f"%(ad,bal))
                        # apan yaha time bhi dikha sakte he using tie module
                        # break


                    elif uc == 2:
                        # Functon for amount withdrow
                        aw = int(input("Enter the amount that you want to withdrow: "))
                        if bal>aw:
                            bal = bal - aw
                            print("Your updated Amount is %.2f"%(bal))
                        else:
                            print("You are not having that much Amount")
                    
                    # Function for cheak Balance
                    elif uc == 3:
                        print("Your Balance is %.2f"%bal)
                        # break


                    # Calling the fuction Change pin
                    elif uc==4:
                        change_pin(id)

                    # Calling the fuction Add Account
                    elif uc==5:
                        add_acc(customer)

                    # Calling the fuction admin
                    elif uc==100:
                        admin()

                    # Exit Fuction
                    elif uc==0:
                        print("Thanks For Visiting\n")
                        # sys.exit()
                        break
                    
                    
                    

                    else:
                        print("Enter Valid Number")
                
            else:
                print("Please Enter Correct PIN")
                # input("")
                # sleep(3)
                # system('cls')

        else:
            print("Your account ID is not Available here...\nPlease ReEnter Your Id\n\nOR Make a new Acount")
            k = int(input("Enter 123 if you want to make new account\nOr 1 to ReEnter Your Id"))
            if k == 123:
                add_acc(customer)
    else:
        print("---------------------")
        print("Thanks For Visiting\n")
        print("---------------------")
        system('cls')
        break




print("Waiting for new Customer...")        
# print("Thank")
sleep(2)
system('cls')
    

# there are many case remain you can test it by yourself.......... 
# thanks for watching.......
# Have a great day........ 


