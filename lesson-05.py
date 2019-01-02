#!/usr/bin/env python3

# lesson-05.py - factor show balance
#
# Learn:
#     more factoring

def showBalance():
    global balance
    print('Your balance is $%d.' % balance)
    print()

balance = 100
print('Welcome to the bank.')
showBalance()

def withdrawal(amount):
    global balance
    print('Withdraw $%d.' % amount)
    balance -= amount
    showBalance()

def deposit(amount):
    global balance
    print('Deposit $%d.' % amount)
    balance += amount
    showBalance()

withdrawal(10)
deposit(20)
withdrawal(30)
deposit(15)
