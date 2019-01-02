#!/usr/bin/env python3

# lesson-21.py - create Account class with static balance member instead of passing around
#
# Learn:
#     class definition
#     static (class) members and access to them
#     variable and method members
#     another way to avoid globals

import sys

class Account:
    balance = None
    startingBalance = None
    transactions = []

    def initBalance(balance):
        Account.balance = balance
        Account.startingBalance = balance

    def showBalance():
        print('Your balance is $%d.' % Account.balance)
        print()

    def showTransactions():
        balance = Account.startingBalance
        print('   op      amount  balance')
        print('--------  -------  -------')
        print('                   %7d  (starting)' % balance)
        for transaction in Account.transactions:
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
        if amount > Account.balance:
            print("Sorry, you don't have that much!")
        else:
            print('Withdraw $%d.' % amount)
            Account.balance -= amount
            Account.transactions.append(['w', amount])
            Account.showBalance()

    def deposit(amount):
        print('Deposit $%d.' % amount)
        Account.balance += amount
        Account.transactions.append(['d', amount])
        Account.showBalance()

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

def getStartingBalance(balance):
    if len(sys.argv) > 1:
        try:
            balance = int(sys.argv[1])
            if balance < 0:
                print('The balance cannot be negative.')
                balance = None
        except:
            print('Invalid starting balance.')
            print('usage: %s [amount]' % sys.argv[0])
            print('where amount is a starting balance dollar amount')
            balance = None
    return balance

def processTransactions():
    while True:
        amount = None
        op = getOperation()
        if op == 'q':
            break
        elif op == 't':
            Account.showTransactions()
        elif op is not None:
            amount = getAmount()

        if amount is None:
            pass
        elif op == 'd':
            Account.deposit(amount)
        else:
            Account.withdrawal(amount)

def main():
    balance = 100
    balance = getStartingBalance(balance)

    if balance is not None:
        print('Welcome to the bank.')
        Account.initBalance(balance)
        Account.showBalance()
        processTransactions()

main()
