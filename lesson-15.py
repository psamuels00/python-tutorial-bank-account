#!/usr/bin/env python3

# lesson-15.py - fix bug
#
# Learn:
#     the importance of initializing reused variables sometimes
#     why testing is important

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

def getType():
    type = input('Enter d for deposit, w for withdrawal, or q to quit: ')
    if type != 'q' and type != 'd' and type != 'w':
        print('Invalid type.  Please try again.')
        type = None
    return type

def getAmount():
    amount = None
    try:
        amount = int(input('Enter amount: '))
        if amount <= 0:
            print('The amount must be positive.')
            amount = None
    except:
        print('Invalid amount.  Please try again.')

    return amount

def main():
    print('Welcome to the bank.')
    showBalance()

    while True:
        amount = None   # <--- needed in case amount gets set on one iteration and then user supplies invalid type on next iteration
        type = getType()
        if type == 'q':
            break
        elif type is not None:
            amount = getAmount()

        if amount is None:
            pass
        elif type == 'd':
            deposit(amount)
        else:
            withdrawal(amount)

balance = 100
main()
