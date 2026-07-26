from pathlib import Path
import random
import string
import json

class bank:
     __data=[]
     __database="data.json"
     try:
          if Path(__database).exists:
               with open(__database) as f:
                    __data=json.load(f)
          else:
               print("path not exist!")
     except Exception as e:
          print(f"{e} occured!")

     @classmethod
     def __update(cls):
          try:
               if Path(cls.__database).exists:
                    with open(cls.__database,'w') as f:
                         json.dump(bank.__data,f)
               else:
                    print("path not exist!")
          except Exception as e:
               print(f"{e} occured!")

     @classmethod
     def __generate_acc_no(cls):
          alpha=random.choices(string.ascii_letters, k=4)
          specialcharacters=random.choices("/@#$%^&*",k=4)
          numbers=random.choices("123456789",k=6)
          concat=alpha=specialcharacters+numbers
          random.shuffle(concat)
          return "".join(concat)



     def createaccount(self):
          user={
               "name":input("enter your name: "),
               "age" :int(input("enter your age: ")),
               "phone":int(input("enter your phone number: ")),
               "pin" :int(input("create a 4 digit pin: ")),
               "acc.no":bank.__generate_acc_no(),
               "balance":0
          }
          if user["age"]<18 or len(str(user["phone"]))<10 or len(str(user["pin"]))<4:
               print("can't create account. something went wrong!" \
               "please try to re-enter your information correctly")
          else:
               print('\n')
               for i in user : print(f"{i} : {user[i]}")
               print("\nAccount created successfully!" \
               "please note your account number for future operations\n")
               bank.__data.append(user)
               bank.__update()

     def depositmoney(self):
          try:
               accno=input("enter your account number: ")
               pin=int(input("enter your account pin: "))
               for i in bank.__data:
                    if i["acc.no"]==accno and i["pin"]==pin:
                         amount=int(input("enter amount to deposit: "))
                         i["balance"]+=amount
                         print("amount deposited successfully!")
                    else:
                         continue
                    break
               bank.__update()
          except Exception as e:
               print(f"{e} occured!")

     def withdrawmoney(self):
          try:
               accno=input("enter your account number: ")
               pin=int(input("enter your account pin: "))
               for i in bank.__data:
                    if i["acc.no"]==accno and i["pin"]==pin:
                         print(f"your currect account balance is: {i["balance"]} -/PKR")
                         amount=int(input("enter amount to withdraw: "))
                         i["balance"]-=amount
                         print("\namount withdrawn successfully!\n")
                         print(f"your account balance remaining is: {i["balance"]} -/PKR\n")
                    else:
                         continue
                    break
               bank.__update()
          except Exception as e:
               print(f"{e} occured!")
          

          



user=bank()
print("\nWELCOME TO BANK MANAGEMENT SYSTEM!\n")
print("press 1 to create account")
print("press 2 to withdraw money")
print("press 3 to deposit money")
print("press 4 to check details")
print("press 5 to update details")
print("press 6 to delete account\n")
choice=int(input("enter you choice: "))
if choice==1:
     user.createaccount()
if choice==2:
     user.withdrawmoney()
if choice==3:
     user.depositmoney()
if choice==4:
     pass
if choice==5:
     pass
if choice==6:
     pass
