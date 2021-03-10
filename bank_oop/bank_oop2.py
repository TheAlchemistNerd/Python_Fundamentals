from typing import Dict
from random import randint


def read_int(prompt_msg, error_msg):
    while True:
        try:
            return int(input(prompt_msg))
        except ValueError:
            print(error_msg)


class SavingsAccount:
    def __init__(self, balance):
        self.account_no = ''.join(["{}".format(randint(0, 9)) for num in range(0, 5)])
        self.balance = balance

    def print_account_no(self):
        print("Your account number is {}.".format(self.account_no))

    def display_balance (self):
        print("You currently have £{} in your account.".format(self.balance))

    def read_withdraw_amount(self):
        while True:
            withdraw = read_int("How much money would you like to withdraw?", "This value must be an integer.")
            if withdraw > self.balance:
                print("Sorry, you do not have enough money in your account.")
            else:
                return withdraw

    def withdraw_money(self):
        withdraw = self.read_withdraw_amount()
        print("You have successfully withdrawn £{}.".format(withdraw))
        self.balance -= withdraw
        self.display_balance()

    def deposit_money (self):
        deposit = read_int("How much money would you like to deposit?", "This value must be an integer.")
        print("You have successfully deposited £{}.".format(deposit))
        self.balance += deposit
        self.display_balance()


class Bank:
    def __init__ (self):
        self.savingsAccount: Dict[str, SavingsAccount] = {}

    def create_account(self):
        name = input("Please input your full name: ")
        deposit = read_int("Please input the amount of your initial deposit: ", "Please input a valid integer amount. ")
        print("You have deposited £{}".format(deposit))
        account = SavingsAccount(deposit)
        self.savingsAccount[name] = account
        account.print_account_no()

    def access_account(self):
        while True:
            name = input("Please input your full name: ")
            if name in self.savingsAccount.keys():
                account = self.savingsAccount[name]
                while True:
                    account_no = input("Please enter your account number: ")
                    if account.account_no == account_no:
                        break
                    else:
                        print("There is no such account number associated with this name.")
                break
            else:
                print("We cannot find this name in our system.")
        return account


class BankMenu:
    def __init__(self, bank: Bank):
        self.bank = bank

    def do_bank_menu(self):
        while True:
            choice = input("Enter 1 to create an account.\n"
                           "Enter 2 to access an existing account.\n"
                           "Enter 3 to exit.\n")
            if choice not in ["1", "2", "3"]:
                print ("Please enter 1, 2 or 3..")
            else:
                return choice

    def do_account_menu(self):
        while True:
            choice = input("Enter 1 to display balance.\n"
                           "Enter 2 to withdraw money.\n"
                           "Enter 3 to deposit money.\n"
                           "Enter 4 to return to the main menu.\n")
            if choice not in ["1", "2", "3", "4"]:
                print ("Please enter 1, 2, 3 or 4.")
            else:
                break
        return choice

    def previous_page(self):
        while True:
            return input("Would you like to return to the previous page? Enter yes or no:")[0].lower() == 'y'

    def run(self):
        print("Welcome to the bank!")
        while True:
            user_choice = self.do_bank_menu()
            if user_choice == "1":
                self.bank.create_account()
                if not self.previous_page():
                    break
            elif user_choice == "2":
                account = self.bank.access_account()
                while True:
                    user_choice = self.do_account_menu()
                    if user_choice == "1":
                        account.display_balance()
                    elif user_choice == "2":
                        account.withdraw_money()
                    elif user_choice == "3":
                        account.deposit_money()
                    elif user_choice == "4":
                        break
                    else:
                        continue

                    if not self.previous_page():
                        break
            else:
                break


def main():
    print("Welcome to the bank!")
    bank = Bank()
    bank_menu = BankMenu(bank)
    bank_menu.run()
    print("Thank you for using the bank!")


if __name__ == "__main__":
    main()