import number
from exampleSolution import multiply
# from solutionDom import multiply

solution = 'exampleSolution.py'

testCases = '''
0 0
0 1
1 1
1 1000
100 1000
3 64
5 37
7 37
64 64
15 1224
'''.strip().split('\n')
testCases = [ tuple(map(int, line.split()))  for line in testCases ]
testCases.append((2**7-1, 2**6-1))

# extend by negating
extendedCases = []
for a,b in testCases:
    extendedCases.append(( a, b))
    extendedCases.append((-a, b))
    extendedCases.append(( a,-b))
    extendedCases.append((-a,-b))
testCases = extendedCases

# extend by swapping
extendedCases = []
for a,b in testCases:
    extendedCases.append((a,b))
    extendedCases.append((b,a))
testCases = extendedCases

testCases = sorted(set(testCases), key=lambda (a,b): a*b, reverse=False)

costs           = [  1.0,   1.0,      1.0,      1.0,          0.01,]
standardColumns = ['add', 'sub', 'lshift', 'divmod',  'comparison',]
def formatCounter(counter):
    out = ''
    out += '{:>12} '.format( sum(( cost * counter[col] for cost, col in zip(costs, standardColumns))) )
    for col in standardColumns:
        out += '{:>12} '.format(counter[col])
        del counter[col]
    if counter:
        out += str(counter)
    return out

print ' '*34,
print '{:>12}'.format('cost'),
for col in standardColumns:
    print '{:>12}'.format(col),
print
for a,b in testCases:

    number.counts.clear()

    result = multiply(number.Integer(a), number.Integer(b))
    assert result._int == a * b, '{} * {} = {}  you returned {}'.format(a,b, a*b, result)
    print '{:>5}  * {:>5}  = {:>10}       {}'.format(a,b, result._int, formatCounter(number.counts))
