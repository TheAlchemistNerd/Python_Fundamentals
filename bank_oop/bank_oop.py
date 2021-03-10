from random import randint

class Bank():

    def __init__(self):
        self.savingsAccount ={}

    def create_account(self):

        self.name = input("Please input your full name: ")
        while True:
            try:
                self.deposit = int(input("Please input the amount of your initial deposit: "))
            except:
                print("Please input a valid integer amount. ")
            else:
                print ("You have deposited £{}".format(self.deposit))
                break
        self.accountno = ''.join(["{}".format(randint(0, 9)) for num in range(0, 5)])
        print ("Your account number is {}.".format(self.accountno))
        self.savingsAccount[self.name] = [self.accountno, self.deposit]



    def access_account(self):

        while True:
            self.name = input("Please input your full name: ")
            if self.name in self.savingsAccount.keys():
                while True:
                    self.accountno = input("Please enter your account number: ")
                    if self.accountno == self.savingsAccount[self.name][0]:
                        break
                    else:
                        print ("There is no such account number associated with this name.")
                break
            else:
                print ("We cannot find this name in our system.")



    def display_balance (self):

        print ("You currently have £{} in your account.".format(self.savingsAccount[self.name][1]))


    def withdraw_money (self):

        while True:
            try:
                withdraw = int(input("How much money would you like to withdraw?")) 
            except ValueError:
                print ("This value must be an integer.")
            else:
                if withdraw <= self.savingsAccount[self.name][1]:
                    print ("You have successfully withdrawn £{}.".format(withdraw))
                    self.savingsAccount[self.name][1] -= withdraw
                    self.display_balance()
                    break
                else: 
                    print ("Sorry, you do not have enough money in your account.")


    def deposit_money (self):

        while True:
            try:
                deposit = int(input("How much money would you like to deposit?")) 
            except ValueError:
                print ("This value must be an integer.")
            else:
                print ("You have successfully deposited £{}.".format(deposit))
                self.savingsAccount[self.name][1] += deposit
                self.display_balance()
                break    



def user_choice1():  

    while True:
        choice1 = input("Enter 1 to create an account.\nEnter 2 to access an existing account.\nEnter 3 to exit.\n")
        if choice1 not in ["1", "2", "3"]:
            print ("Please enter 1, 2 or 3..")
        else:
            break
    return choice1


def user_choice2():

    while True:
        choice2 = input("Enter 1 to display balance.\nEnter 2 to withdraw money.\nEnter 3 to deposit money.\nEnter 4 to return to the main menu.\n")
        if choice2 not in ["1", "2", "3", "4"]:
            print ("Please enter 1, 2, 3 or 4.")
        else:
            break

    return choice2 



def previous_page ():

    while True:
        return input("Would you like to return to the previous page? Enter yes or no:")[0].lower() == 'y'

print ("Welcome to the bank!")   
bank=Bank()
while True:
    userchoice1 = user_choice1()
    if userchoice1 == "1":
        bank.create_account()
        if not previous_page():
            break
        else:
            continue
    elif userchoice1 == "2": 
        bank.access_account()     
        while True:
            userchoice2 = user_choice2()
            if userchoice2 == "1":
                bank.display_balance()
                if not previous_page():
                    break
                else:
                    continue 
            elif userchoice2=="2":   
                bank.withdraw_money()   
                if not previous_page():
                    break
                else:
                    continue 
            elif userchoice2=="3":
                bank.deposit_money()
                if not previous_page():
                    break
                else:
                    continue
            elif userchoice2=="4":
                break
    else:
        break

print ("Thank you for using the bank!")
