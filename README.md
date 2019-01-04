Python Tutorial - Bank Account
==============================

This tutorial was designed for an absolute beginner to learn about programming using Python.
The first lesson starts off very simple.  With each subsequent lesson, we add a feature or
improve the code one step at a time so that by the end, we have a small Bank Account program
with the following features:

* Initial account balance can be set on startup
* Interactive user input
* Deposit into account
* Withdraw from account
* List all transactions

A simple transaction list might look like this:

```
      op       amount     balance
   --------  ----------  ----------
                              50.00  (starting)
   deposit        15.00       65.00
   deposit       125.01      190.01
   withdraw       25.00      165.01
```


Requirements
------------

* Python 3
* A text editor or IDE (Integrated Development Environment)
* A shell to execute your scripts from

PyCharm is an excellent choice of an IDE to use.  The Community Edition is free.
It has a built in shell and debugger for running your scripts, as well as many other features.

This tutorial is not complete as-is.  You will need an experienced programmer
to explain the concepts that are to be learned for each lesson.


Bank Account
------------

The `bank_account.py` file contains all the lessons in its revision history.  It is the same
as `lesson-26.py` except that it is missing the comments at top.  Since this file was updated
incrementally to reflect the latest lesson as it was added to the repository, you can easily
see what has changed by looking at the commit differences for this file.


Lessons Summary
---------------

For each lesson, there is an essential enhancement to be made, as well as a set
of Python features or programming concepts to be learned.  To follow the tutorial,
read the lesson summary below and then study the corresponding .py file.  Better
yet, try to implement the enhancement on your own and use the provided .py file
as a guide when you get stuck.


#### Lesson 0

Print hello world.

* shebang line
* single-line comments
* string literal
* print statement
* function and function call

#### Lesson 1

Welcome to the bank and show account balance.

* integer and string literals
* variable
* assignment operator
* format operator
* format integer field
* expression

#### Lesson 2

Show a $10 withdrawal and a $20 deposit.

* print empty line
* compound assignment operators

#### Lesson 3

Show a $30 withdrawal and a $15 deposit.

* the tedium of repetition

#### Lesson 4

Factor both withdrawals and factor both deposits.

* function definition
* function calling
* code factoring
* global variables
* indentation

#### Lesson 5

Factor show balance.

* more factoring

#### Lesson 6

Reorder code to group functions.

* code reorg: functions first
* function with no arguments

#### Lesson 7

Create function for main code.

* code reorg: more function grouping

#### Lesson 8

Allow user to supply transaction amounts.

* user input
* string conversion to integer

#### Lesson 9

Have only 1 transaction, but allow user to determine which type.

* string input and equality comparison
* conditional statement with else clause (branching)

#### Lesson 10

Allow unlimited transactions.

* looping
* break out of a loop
* Boolean literal
* single-branch conditional statement

#### Lesson 11

Add error checking for each prompt.

* error checking
* syntax errors
* exception handling
* continue statement to skip rest of loop
* inequality comparison
* "and" logical operator

#### Lesson 12

Add semantic error checking for transaction.

* semantic errors
* ordering comparison
* single-quotes vs double-quotes

#### Lesson 13

Flatten the logic in main().

* code reorg: reduce nesting

#### Lesson 14

Refactor again and simplify main().

* None object
* is operator
* pass statement
* else-if clause of conditional statement
* "not" logical operator

#### Lesson 15

Fix bug.

* the importance of initializing reused variables sometimes
* why testing is important

#### Lesson 16

Rename 'type' to 'op' for operator.

* the importance of naming
* identifiers sometimes need to change as code evolves

#### Lesson 17

Keep a log of all transactions and list them using 't' op.

* list data structure and list of lists
* empty list literal
* append to a list
* iterate over a list
* get size of list
* for loop
* format field width

#### Lesson 18

Show starting and running balance with transactions.

* list assignment to variables (spread?)
* format string field
* format field left alignment
* tuple as operand for format operator
* use of second variable to save initial value

#### Lesson 19

Get starting account balance from command line argument, including error handling.

* module import and the sys module
* access to program arguments

#### Lesson 20

Eliminate global variable by passing around balance.

* avoid globals by passing variables
* keep global space unpolluted

#### Lesson 21

Create Account class with static balance member instead of passing around.

* class definition
* static (class) members and access to them
* variable and method members
* another way to avoid globals

#### Lesson 22

Make balance an instance member and instantiate the class.

* class instantiation
* objects and object-oriented programming
* the class constructor
* instance members and access to them
* the self reference
* passing objects as parameters

#### Lesson 23

Use float for amounts instead of int; update error checking and output format.

* float literal
* string conversion to float
* format float field
* format field precision
* prevent accumulation error
* the regular expression module and re pattern matching
* raise an exception
* distinguish different types of exception (ValueError, Exception)
* how diligent you must be with floats

#### Lesson 24

Clean up and refactor more.

* more refactoring
* re-raise an exception

#### Lesson 25

Add name to account, create multiple instances of account and test transactions.

* testing
* instrumenting code to assist with testing
* multiple instantiation of a class
* default parameter value
* program startup flag
* program exit code

automate from the command line, for example:
* printf "w\n.02\nd\n125.32\nw\n100\nd\n1\nt\nq\n" | ./take-25.py 100.01; echo

#### Lesson 26

Use set to validate op.

* set data structure and set inclusion
* string expansion


Floating Point Calculations
---------------------------

The file `float_error/test.py` is included to demonstrate the challenges of floating point
calculations.  The file `float_error/output.txt` contains the output of running this.


Errata
------

#### Lessons Summary Generation

    grep '^#' *.py | cut -d'#' -f2 | cut -c2- | grep -v '^Learn:' | perl -pe 's|/usr/bin/env python3||; s|(lesson-(..).py - )(.*)|sprintf qq(### Lesson %d\n\n%s.), $2, ucfirst($3)|e; s|^    |* |'


#### Commit and Tag All Lessons

    update_lesson() {
        n=$1
        cat lesson-$n.py | sed '3,/^$/ d' > bank-account.py
        git add lesson-$n.py bank-account.py
        git commit -m "add lesson $n"
        git tag lesson-$n
    }

    for x in {0..26}; do
        x=`printf '%02d' $x`
        echo $x
        update_lesson $x
    done

    git push
    git push --tags
