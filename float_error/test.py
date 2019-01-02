#!/usr/bin/env python3

def testWithTruncate(amountStr, truncateSum):
    amount = float(amountStr)
    sum = 0.0
    for i in range(100 * 1000):
        sum += amount
        if truncateSum:
            sum = float('%.2f' % sum)
    trunc = 'truncate sum' if truncateSum else 'accumul8 sum'
    print("for '%s' %s, sum = %.10f, %.2f" % (amountStr, trunc, sum, sum))
    return sum

def test(amountStr):
    sumWithoutTruncate = testWithTruncate(amountStr, False)
    sumWithTruncate = testWithTruncate(amountStr, True)
    print()

for i in range(20):
    test('%.2f' % (i/100))

