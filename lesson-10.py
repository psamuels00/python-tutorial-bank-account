#!/usr/bin/env python3

# lesson-10.py - allow unlimited transactions
#
# Learn:
#     looping
#     break out of a loop
#     Boolean literal
#     single-branch conditional statement

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

    while True:
        type = input('Enter d for deposit, w for withdrawal, or q to quit: ')
        if type == 'q':
            break
        amount = int(input('Enter amount: '))
        if type == 'd':
            deposit(amount)
        else:
            withdrawal(amount)

balance = 100
main()
