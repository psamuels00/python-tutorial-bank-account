#!/usr/bin/env python3

# lesson-17.py - keep a log of all transactions and list them using 't' op
#
# Learn:
#     list data structure and list of lists
#     empty list literal
#     append to a list
#     iterate over a list
#     get size of list
#     for loop
#     format field width

def showBalance():
    global balance
    print('Your balance is $%d.' % balance)
    print()

def showTransactions():
    global transactions
    if len(transactions) > 0:
        print('Transactions')
        print('----------------')
        for transaction in transactions:
            type = transaction[0]
            amount = transaction[1]
            if type == 'w':
                print('withdraw %7d' % amount)
            else:
                print('deposit  %7d' % amount)
        print()
    else:
        print('There are no transactions yet.')
        showBalance()

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

def main():
    print('Welcome to the bank.')
    showBalance()

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

balance = 100
transactions = []
main()
