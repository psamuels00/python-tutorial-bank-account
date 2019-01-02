#!/usr/bin/env python3

# lesson-16.py - rename 'type' to 'op' for operator
#
# Learn:
#     the importance of naming
#     identifiers sometimes need to change as code evolves

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

def getOperation():
    op = input('Enter d for deposit, w for withdrawal, or q to quit: ')
    if op != 'q' and op != 'd' and op != 'w':
        print('Invalid operation.  Please try again.')
        op = None
    return op

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
        amount = None
        op = getOperation()
        if op == 'q':
            break
        elif op is not None:
            amount = getAmount()

        if amount is None:
            pass
        elif op == 'd':
            deposit(amount)
        else:
            withdrawal(amount)

balance = 100
main()
