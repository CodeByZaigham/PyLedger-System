import streamlit as st
from pathlib import Path
import random
import string
import json

class Bank:
    __data = []
    __database = "data.json"

    if Path(__database).exists():
        with open(__database) as f:
            __data = json.load(f)

    @classmethod
    def __update(cls):
        with open(cls.__database, 'w') as f:
            json.dump(cls.__data, f, indent=4)

    @classmethod
    def __generate_acc_no(cls):
        alpha = random.choices(string.ascii_letters, k=4)
        special = random.choices("/@#$%^&*", k=4)
        numbers = random.choices("123456789", k=6)
        concat = alpha + special + numbers
        random.shuffle(concat)
        return "".join(concat)

    @classmethod
    def create_account(cls, name, age, phone, pin):
        if age < 18 or len(str(phone)) < 10 or len(str(pin)) != 4:
            return False, "Invalid details"

        user = {
            "name": name,
            "age": age,
            "phone": phone,
            "pin": pin,
            "acc.no": cls.__generate_acc_no(),
            "balance": 0
        }

        cls.__data.append(user)
        cls.__update()
        return True, user

    @classmethod
    def find_user(cls, accno, pin):
        for i in cls.__data:
            if i["acc.no"] == accno and i["pin"] == pin:
                return i
        return None

    @classmethod
    def deposit(cls, accno, pin, amount):
        user = cls.find_user(accno, pin)
        if not user:
            return False, "User not found"
        if amount <= 0 or amount > 100000:
            return False, "Invalid amount"

        user["balance"] += amount
        cls.__update()
        return True, "Deposited successfully"

    @classmethod
    def withdraw(cls, accno, pin, amount):
        user = cls.find_user(accno, pin)
        if not user:
            return False, "User not found"
        if amount <= 0 or amount > user["balance"]:
            return False, "Invalid amount"

        user["balance"] -= amount
        cls.__update()
        return True, "Withdraw successful"

    @classmethod
    def delete_account(cls, accno, pin):
        user = cls.find_user(accno, pin)
        if not user:
            return False, "User not found"

        cls.__data.remove(user)
        cls.__update()
        return True, "Account deleted"

st.title("🏦 Bank Management System")

menu = ["Create Account", "Deposit", "Withdraw", "Check Details", "Delete Account"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Create Account":
    st.subheader("Create Account")

    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1)
    phone = st.text_input("Phone")
    pin = st.text_input("4-digit PIN", type="password")

    if st.button("Create"):
        success, result = Bank.create_account(name, age, phone, pin)
        if success:
            st.success("Account Created!")
            st.write(result)
        else:
            st.error(result)

elif choice == "Deposit":
    st.subheader("Deposit Money")

    accno = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Deposit"):
        success, msg = Bank.deposit(accno, pin, amount)
        if success:
            st.success(msg)
        else:
            st.error(msg)

elif choice == "Withdraw":
    st.subheader("Withdraw Money")

    accno = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Withdraw"):
        success, msg = Bank.withdraw(accno, pin, amount)
        if success:
            st.success(msg)
        else:
            st.error(msg)

elif choice == "Check Details":
    st.subheader("Account Details")

    accno = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Check"):
        user = Bank.find_user(accno, pin)
        if user:
            st.write(user)
        else:
            st.error("User not found")

elif choice == "Delete Account":
    st.subheader("Delete Account")

    accno = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Delete"):
        success, msg = Bank.delete_account(accno, pin)
        if success:
            st.success(msg)
        else:
            st.error(msg)