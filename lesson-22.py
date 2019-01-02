#!/usr/bin/env python3

# lesson-22.py - make balance an instance member and instantiate the class
#
# Learn:
#     class instantiation
#     objects and object-oriented programming
#     the class constructor
#     instance members and access to them
#     the self reference
#     passing objects as parameters

import sys

class Account:
    def __init__(self, balance):
        self.balance = balance
        self.startingBalance = balance
        self.transactions = []

    def showBalance(self):
        print('Your balance is $%d.' % self.balance)
        print()

    def showTransactions(self):
        balance = self.startingBalance
        print('   op      amount  balance')
        print('--------  -------  -------')
        print('                   %7d  (starting)' % balance)
        for transaction in self.transactions:
            [op, amount] = transaction
            if op == 'w':
                opLabel = 'withdraw'
                balance -= amount
            else:
                opLabel = 'deposit'
                balance += amount
            print('%-8s  %7d  %7d' % (opLabel, amount, balance))
        print()

    def withdrawal(self, amount):
        if amount > self.balance:
            print("Sorry, you don't have that much!")
        else:
            print('Withdraw $%d.' % amount)
            self.balance -= amount
            self.transactions.append(['w', amount])
            self.showBalance()

    def deposit(self, amount):
        print('Deposit $%d.' % amount)
        self.balance += amount
        self.transactions.append(['d', amount])
        self.showBalance()

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

def processTransactions(account):
    while True:
        amount = None
        op = getOperation()
        if op == 'q':
            break
        elif op == 't':
            account.showTransactions()
        elif op is not None:
            amount = getAmount()

        if amount is None:
            pass
        elif op == 'd':
            account.deposit(amount)
        else:
            account.withdrawal(amount)

def main():
    balance = 100
    balance = getStartingBalance(balance)

    if balance is not None:
        print('Welcome to the bank.')
        account = Account(balance)
        account.showBalance()
        processTransactions(account)

main()
