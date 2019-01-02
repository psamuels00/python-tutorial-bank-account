#!/usr/bin/env python3

# lesson-09.py - have only 1 transaction, but allow user to determine which type
#
# Learn:
#     string input and equality comparison
#     conditional statement with else clause (branching)

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

    type = input('Enter d for deposit, w for withdrawal: ')
    amount = int(input('Enter amount: '))
    if type == 'd':
        deposit(amount)
    else:
        withdrawal(amount)

balance = 100
main()
