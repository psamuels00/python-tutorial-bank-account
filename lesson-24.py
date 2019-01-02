#!/usr/bin/env python3

# lesson-24.py - clean up and refactor more
#
# Learn:
#     more refactoring
#     re-raise an exception

import re
import sys

class Account:
    def __init__(self, balance):
        self.balance = balance
        self.startingBalance = balance
        self.transactions = []

    def showBalance(self):
        print('Your balance is $%0.2f.' % self.balance)
        print()

    def showTransactions(self):
        balance = self.startingBalance
        print('   op       amount     balance')
        print('--------  ----------  ----------')
        print('                      %10.2f  (starting)' % balance)
        for transaction in self.transactions:
            [op, amount] = transaction
            if op == 'w':
                opLabel = 'withdraw'
                balance -= amount
            else:
                opLabel = 'deposit'
                balance += amount
            print('%-8s  %10.2f  %10.2f' % (opLabel, amount, balance))
        print()

    def withdrawal(self, amount):
        if amount > self.balance:
            print("Sorry, you don't have that much!")
        else:
            print('Withdraw $%0.2f.' % amount)
            self.balance = float('%.2f' % (self.balance - amount))  # prevent accumulation error
            self.transactions.append(['w', amount])
            self.showBalance()

    def deposit(self, amount):
        print('Deposit $%0.2f.' % amount)
        self.balance = float('%.2f' % (self.balance + amount))  # prevent accumulation error
        self.transactions.append(['d', amount])
        self.showBalance()

    def processTransactions(account):
        while True:
            amount = None
            op = Input.getOperation()
            if op == 'q':
                break
            elif op == 't':
                account.showTransactions()
            elif op is not None:
                amount = Input.getAmount()

            if amount is None:
                pass
            elif op == 'd':
                account.deposit(amount)
            else:
                account.withdrawal(amount)

class Input:
    def getOperation():
        op = input('Enter d for deposit, w for withdrawal, t for transactions, or q to quit: ')
        if op != 'q' and op != 'd' and op != 'w' and op != 't':
            print('Invalid operation.  Please try again.')
            op = None
        return op

    def validateDollarAmount(amountStr):
        tooMuchPrecision = re.compile('.*\.\d\d\d.*')
        if tooMuchPrecision.match(amountStr):
            raise Exception('You cannot supply fractions of a cent.')

    def getAmount():
        amount = None
        try:
            value = input('Enter amount: ')
            amount = float(value)
            if amount <= 0:
                raise Exception('The amount must be positive.')
            Input.validateDollarAmount(value)
        except ValueError:
            print('Invalid amount.  Please try again.')
        except Exception as e:
            print(e)
            amount = None

        return amount

class App:
    defaultBalance = 0.0

    def usage():
        print('usage: %s [amount]' % sys.argv[0])
        print('where amount is a starting balance dollar amount')

    def getStartingBalance():
        balance = App.defaultBalance
        if len(sys.argv) > 2:
            raise Exception('Unrecognized arguments.')
        elif len(sys.argv) == 2:
            try:
                value = sys.argv[1]
                balance = float(value)
                if balance < 0:
                    raise Exception('The balance cannot be negative.')
                Input.validateDollarAmount(value)
            except ValueError:
                raise Exception('Invalid starting balance. Try something like 17.25 or 0 (the default).')
        return balance

    def run():
        try:
            balance = App.getStartingBalance()
            print('Welcome to the bank.')
            account = Account(balance)
            account.showBalance()
            account.processTransactions()
        except Exception as e:
            print(e)
            App.usage()

def main():
    App.run()

main()

