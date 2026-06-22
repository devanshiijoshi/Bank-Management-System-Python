import random
import json
from pathlib import Path


class Bank:

    file = 'user_info.json'
    data = []

    try:
        if Path(file).exists():
            with open(file) as fs:
                data = json.loads(fs.read())
        else:
            print("Sorry no such file exsists")
    except Exception as err:
        print(f"Sorry an error occured as {err}")

    @classmethod
    def __generate_acc_no(cls):
        while True:
            acc_num = random.randint(100000,999999)
            if not any(
                user['account_no.'] == acc_num
                for user in Bank.data
                ):
                return acc_num
    
    @classmethod
    def __update(cls):
        with open(Bank.file,'w') as fs:
            fs.write(json.dumps(Bank.data))

    def create_acc(self):
        info = {
            "name" : input("please enter your name : "),
            "age" : int(input("please enter your age : ")),
            "email" : input("please enter your email : "),
            "account_no." : Bank.__generate_acc_no(),
            "pin" : int(input("please enter your 4 digit pin : ")),
            "balance" : 0
        }

        if len(str(info['pin'])) != 4:
            print("sorry pin must be 4 digit only")

        else:
            print("Account created successfully")
            print("Here are your details : \n")
            for i in info:
                print(f"{i} : {info[i]}")

            Bank.data.append(info)
            Bank.__update()
            


    def deposit_money(self):
        acc_no = int(input("Please enter your account number : "))
        pin = int(input("Please tell your pin : "))

        userdata = [i for i in Bank.data if i['account_no.'] == acc_no and i['pin'] == pin]

        if not userdata:
            print("Invalid account number or pin")

        else:
            amount = int(input("Please enter the amount you want to deposit : "))

            if amount <= 0:
                print("Invalid amount")

            else:
                userdata[0]['balance'] += amount
                print("\n Amount deposited successfully ")
                Bank.__update()

    def withdraw_money(self):
        acc_no = int(input("Please enter your account number : "))
        pin = int(input("Please enter your pin : "))

        userdata = [i for i in Bank.data if i['account_no.'] == acc_no and i['pin'] == pin]

        if not userdata:
            print("Invalid account number or pin")

        else:
            amount = int(input("Enter amount you want to withdraw : "))

            if amount > userdata[0]['balance']:
                print(f"Transaction Failed : Insufficient Balance, Current Balance is Rs.{userdata[0]['balance']}")

            else:
                userdata[0]['balance'] -= amount
                print(f"Transaction Successful : Amount Withdrawn : Rs.{amount}")
                Bank.__update();

    def show_details(self):
        acc_no = int(input("Please enter your account number : "))
        pin = int(input("Please enter your pin : "))

        userdata = [i for i in Bank.data if i['account_no.'] == acc_no and i['pin'] == pin]

        if not userdata:
            print("Invalid Account number or pin")

        else:
            print("Here are your details : \n")
            for i in userdata[0]:
                print(f"{i} : {userdata[0][i]}")
            print("\n")

    def update_details(self):
        acc_no = int(input("Please enter your account number : "))
        pin = int(input("please eneter your pin : "))

        userdata = [i for i in Bank.data if i['account_no.'] == acc_no and i['pin'] == pin]

        if not userdata:
            print("Invalid account number or pin")

        else:
            print("fill the details or leave empty if no change ")

            new_data = {
                "name" : input("Please enter new name or press enter to skip it : "),
                "email" : input("please enter new email or press enter to skip it : "),
                "pin" : input("Please enter new pin or press enter to skip it : ")
            }

            if new_data["name"] == "":
                new_data["name"] = userdata[0]['name']

            if new_data["email"] == "":
                new_data["email"] = userdata[0]['email']

            if new_data["pin"] == "":
                new_data["pin"] = userdata[0]['pin']

            new_data["age"] = userdata[0]['age']
            new_data["account_no."] = userdata[0]['account_no.']
            new_data["balance"] = userdata[0]['balance']

            if type(new_data["pin"]) == str:
                new_data["pin"] = int(new_data["pin"])

            for i in new_data:
                if new_data[i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i] = new_data[i]

            Bank.__update()
            print("Details updated successfully")


    def delete_acc(self):
        acc_no = int(input("Please enter your account number : "))
        pin = int(input("please eneter your pin : "))

        userdata = [i for i in Bank.data if i['account_no.'] == acc_no and i['pin'] == pin]

        if not userdata:
            print("Invalid account number or pin")

        else:
            check = input("Are you sure you want to delete your account? (Y/N) : ")
            if check == 'N' or check == 'n':
                print("Account Deletion Cancelled")
            else:
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("Account deleted successfully")
                Bank.__update()

user = Bank()

print("press 1 for creating an account")
print("press 2 for depositing money")
print("press 3 for withdrawing money")
print("press 4 to view account details")
print("press 5 for updating the details")
print("press 6 for deleting your account")

check = int(input("please enter your response : "))

if check == 1:
    user.create_acc()

if check == 2:
    user.deposit_money()

if check == 3: 
    user.withdraw_money()

if check == 4:
    user.show_details()

if check == 5:
    user.update_details()

if check == 6:
    user.delete_acc()