#!/usr/bin/env python3

# lesson-12.py - add semantic error checking for transaction
#
# Learn:
#     semantic errors
#     ordering comparison
#     single-quotes vs double-quotes

def showBalance():
    global balance
    print('Your balance is $%d.' % balance)
    print()

def withdrawal(amount):
    global balance
    if amount > balance:
        print("Sorry, you don't have that much!")
    else:
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
            continue;
        else:
            try:
                amount = int(input('Enter amount: '))
            except:
                print('Invalid amount.  Please try again.')
                continue;

        if amount <= 0:
            print('The amount must be positive.')
        elif type == 'd':
            deposit(amount)
        else:
            withdrawal(amount)

balance = 100
main()
