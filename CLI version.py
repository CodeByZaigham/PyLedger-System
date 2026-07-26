from pathlib import Path
import random
import string
import json

class bank:
     __data=[]
     __database="data.json"
     try:
          if Path(__database).exists():
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
          concat=alpha+specialcharacters+numbers
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
               userdata=[i for i in bank.__data if i["acc.no"]==accno and i["pin"]==pin]
               if bool(userdata) == False:
                    print("data not found for required account number")
               else:
                    amount=int(input("enter amount to deposit: "))
                    if amount>100000 or amount<0:
                         print("deposit amount should be between 0-1 lac")
                    else:
                         userdata[0]["balance"]+=amount
                         bank.__update()
                         print("Amount deposited successfully!")
          except Exception as e:
               print(f"{e} occured!")

     def withdrawmoney(self):
          try:
               accno=input("enter your account number: ")
               pin=int(input("enter your account pin: "))
               userdata=[i for i in bank.__data if i["acc.no"]==accno and i["pin"]==pin]
               if bool(userdata) == False:
                    print("data not found for required account number")
               else:
                    print(f"you current account balance is: {userdata[0]['balance']}")
                    amount=int(input("enter amount to withdraw: "))
                    if amount>userdata[0]["balance"] or amount<0:
                         print("withdraw amount should be valid")
                    else:
                         userdata[0]["balance"]-=amount
                         bank.__update()
                         print("Amount withdrawn successfully!")
          except Exception as e:
               print(f"{e} occured!")

     def showdetails(self):
          try:
               accno=input("enter your account number: ")
               pin=int(input("enter your account pin: "))
               userdata=[i for i in bank.__data if i["acc.no"]==accno and i["pin"]==pin]
               if bool(userdata) == False:
                    print("data not found for required account number")
               else:
                    user=userdata[0]
                    for i in user: print(f"{i} : {user[i]}")
          except Exception as e:
               print(f"{e} occured!")

     def updatedetails(self):
          try:
               accno=input("enter your account number: ")
               pin=int(input("enter your account pin: "))
               userdata=[i for i in bank.__data if i["acc.no"]==accno and i["pin"]==pin]
               if bool(userdata) == False:
                    print("data not found for required account number")
               else:
                    user=userdata[0]
                    for i in user: print(f"{i} : {user[i]}")
                    print("\n note that you can only change name,phone number and pin.\n" \
                    "fill out following fields with new data or leave it empty if no change.\n")
                    newdata={
                         "name":input("enter your name: "),
                         "phone":input("enter your phone number: "),
                         "pin" :input("create a 4 digit pin: "),
                    }
                    if newdata["name"]!="":
                         user["name"]=newdata["name"]
                    if newdata["phone"]!="" and newdata["phone"].isdigit():
                         user["phone"]=newdata["phone"]
                    if newdata["pin"]!="" and newdata["pin"].isdigit():
                         user["pin"]=newdata["pin"]

                    bank.__update()
                    print("information updated!")

          except Exception as e:
               print(f"{e} occured!")
          
     def deleteaccount(self):
          try:
               accno=input("enter your account number: ")
               pin=int(input("enter your account pin: "))
               userdata=[i for i in bank.__data if i["acc.no"]==accno and i["pin"]==pin]
               if bool(userdata) == False:
                    print("data not found for required account number")
               else:
                    user=userdata[0]
                    bank.__data.remove(user)
                    bank.__update()
                    print("account removed successfully!")
          except Exception as e:
               print(f"{e} occured!")

#MAIN FUNCTION
          
user=bank()
print("\nWELCOME TO BANK MANAGEMENT SYSTEM!\n")
print("press 1 to create account")
print("press 2 to withdraw money")
print("press 3 to deposit money")
print("press 4 to check details")
print("press 5 to update details")
print("press 6 to delete account\n")
try:
     choice=int(input("enter your choice: "))
     if choice==1:
          user.createaccount()
     if choice==2:
          user.withdrawmoney()
     if choice==3:
          user.depositmoney()
     if choice==4:
          user.showdetails()
     if choice==5:
          user.updatedetails()
     if choice==6:
          user.deleteaccount()
except Exception as e:
     print(f"{e} occured")