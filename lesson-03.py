#!/usr/bin/env python3

# lesson-03.py - show a $30 withdrawal and a $15 deposit
#
# Learn:
#     the tedium of repetition

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

amount = 30
print('Withdraw $%d.' % amount)
balance -= amount
print('Your balance is $%d.' % balance)
print()

amount = 15
print('Deposit $%d.' % amount)
balance += amount
print('Your balance is $%d.' % balance)
print()
