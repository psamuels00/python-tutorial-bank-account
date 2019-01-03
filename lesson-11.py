#!/usr/bin/env python3

# lesson-11.py - add error checking for each prompt
#
# Learn:
#     error checking
#     syntax errors
#     exception handling
#     continue statement to skip rest of loop
#     inequality comparison
#     "and" logical operator

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
        elif type != 'd' and type != 'w':
            print('Invalid type.  Please try again.')
            continue
        else:
            try:
                amount = int(input('Enter amount: '))
            except:
                print('Invalid amount.  Please try again.')
                continue

        if type == 'd':
            deposit(amount)
        else:
            withdrawal(amount)

balance = 100
main()
