#!/usr/bin/env python3

# lesson-07.py - create function for main code
#
# Learn:
#     code reorg: more function grouping

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

    withdrawal(10)
    deposit(20)
    withdrawal(30)
    deposit(15)

balance = 100
main()
