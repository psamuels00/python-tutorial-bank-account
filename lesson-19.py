#!/usr/bin/env python3

# lesson-19.py - get starting account balance from command line argument, including error handling
#
# Learn:
#     module import and the sys module
#     access to program arguments

import sys

def showBalance():
    global balance
    print('Your balance is $%d.' % balance)
    print()

def showTransactions():
    global startingBalance, transactions
    balance = startingBalance
    print('   op      amount  balance')
    print('--------  -------  -------')
    print('                   %7d  (starting)' % balance)
    for transaction in transactions:
        [op, amount] = transaction
        if op == 'w':
            opLabel = 'withdraw'
            balance -= amount
        else:
            opLabel = 'deposit'
            balance += amount
        print('%-8s  %7d  %7d' % (opLabel, amount, balance))
    print()

def withdrawal(amount):
    global balance, transactions
    if amount > balance:
        print("Sorry, you don't have that much!")
    else:
        print('Withdraw $%d.' % amount)
        balance -= amount
        transactions.append(['w', amount])
        showBalance()

def deposit(amount):
    global balance, transactions
    print('Deposit $%d.' % amount)
    balance += amount
    transactions.append(['d', amount])
    showBalance()

def getOperation():
    op = input('Enter d for deposit, w for withdrawal, t for transactions, or q to quit: ')
    if op != 'q' and op != 'd' and op != 'w' and op != 't':
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

def getStartingBalance():
    global balance, startingBalance
    if len(sys.argv) > 1:
        try:
            balance = int(sys.argv[1])
            startingBalance = balance
            if balance < 0:
                print('The balance cannot be negative.')
                balance = None
        except:
            print('Invalid starting balance.')
            print('usage: %s [amount]' % sys.argv[0])
            print('where amount is a starting balance dollar amount')
            balance = None

def processTransactions():
    while True:
        amount = None
        op = getOperation()
        if op == 'q':
            break
        elif op == 't':
            showTransactions()
        elif op is not None:
            amount = getAmount()

        if amount is None:
            pass
        elif op == 'd':
            deposit(amount)
        else:
            withdrawal(amount)

def main():
    getStartingBalance()
    if balance is not None:
        print('Welcome to the bank.')
        showBalance()
        processTransactions()

balance = 100
startingBalance = balance
transactions = []
main()
