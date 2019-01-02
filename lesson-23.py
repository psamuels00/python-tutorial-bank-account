#!/usr/bin/env python3

# lesson-23.py - use float for amounts instead of int; update error checking and output format
#
# Learn:
#     float literal
#     string conversion to float
#     format float field
#     format field precision
#     prevent accumulation error
#     the regular expression module and re pattern matching
#     raise an exception
#     distinguish different types of exception (ValueError, Exception)
#     how diligent you must be with floats

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
        validateDollarAmount(value)
    except ValueError:
        print('Invalid amount.  Please try again.')
    except Exception as e:
        print(e)
        amount = None

    return amount

def usage():
    print('usage: %s [amount]' % sys.argv[0])
    print('where amount is a starting balance dollar amount')

def getStartingBalance(balance):
    if len(sys.argv) > 1:
        try:
            value = sys.argv[1]
            balance = float(value)
            if balance < 0:
                raise Exception('The balance cannot be negative.')
            validateDollarAmount(value)
        except ValueError:
            print('Invalid starting balance. Try something like 17.25 or 100 (the default).')
            usage()
            balance = None
        except Exception as e:
            print(e)
            usage()
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
    balance = 100.0
    balance = getStartingBalance(balance)

    if balance is not None:
        print('Welcome to the bank.')
        account = Account(balance)
        account.showBalance()
        processTransactions(account)

main()

