#!/usr/bin/env python3

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
