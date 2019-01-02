#!/usr/bin/env python3

# lesson-08.py - allow user to supply transaction amounts
#
# Learn:
#     user input
#     string conversion to integer

def showBalance():
    global balance
    print('Your balance is $%d.' % balance)
    print()

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

def main():
    print('Welcome to the bank.')
    showBalance()

    amount = int(input('Enter amount to withdraw: '))
    withdrawal(amount)

    amount = int(input('Enter amount to deposit: '))
    deposit(amount)

    amount = int(input('Enter amount to withdraw: '))
    withdrawal(amount)

    amount = int(input('Enter amount to deposit: '))
    deposit(amount)

balance = 100
main()
