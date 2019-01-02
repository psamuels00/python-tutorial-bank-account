#!/usr/bin/env python3

# lesson-02.py - show a $10 withdrawal and a $20 deposit
#
# Learn:
#     print empty line
#     compound assignment operators

balance = 100
print('Welcome to the bank.')
print('Your balance is $%d.' % balance)
print()

amount = 10
print('Withdraw $%d.' % amount)
balance -= amount
print('Your balance is $%d.' % balance)
print()

amount = 20
print('Deposit $%d.' % amount)
balance += amount
print('Your balance is $%d.' % balance)
print()
