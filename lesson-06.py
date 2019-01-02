#!/usr/bin/env python3

# lesson-06.py - reorder code to group functions
#
# Learn:
#     code reorg: functions first
#     function with no arguments

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

balance = 100

print('Welcome to the bank.')
showBalance()

withdrawal(10)
deposit(20)
withdrawal(30)
deposit(15)
