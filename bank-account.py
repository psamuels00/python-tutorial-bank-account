#!/usr/bin/env python3

balance = 100
print('Welcome to the bank.')
print('Your balance is $%d.' % balance)
print()

def withdrawal(amount):
    global balance
    print('Withdraw $%d.' % amount)
    balance -= amount
    print('Your balance is $%d.' % balance)
    print()

def deposit(amount):
    global balance
    print('Deposit $%d.' % amount)
    balance += amount
    print('Your balance is $%d.' % balance)
    print()

withdrawal(10)
deposit(20)
withdrawal(30)
deposit(15)
