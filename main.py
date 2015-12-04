import number
import exampleSolution

solution = 'exampleSolution.py'

testCases = '''
0 0
0 1
1 1
1 1000
100 1000
3 64
15 1224
'''.strip().split('\n')
testCases = [ tuple(map(int, line.split()))  for line in testCases ]

# # extend by negating
# extendedCases = []
# for a,b in testCases:
#     extendedCases.append(( a, b))
#     extendedCases.append((-a, b))
#     extendedCases.append(( a,-b))
#     extendedCases.append((-a,-b))
# testCases = extendedCases

# extend by swapping
extendedCases = []
for a,b in testCases:
    extendedCases.append((a,b))
    extendedCases.append((b,a))
testCases = extendedCases

testCases = sorted(set(testCases), key=lambda (a,b): a*b, reverse=False)


for a,b in testCases:

    number.counts.clear()

    result = exampleSolution.multiply(number.Integer(a), number.Integer(b))
    assert result._int == a * b, '{} * {} = {}  you returned {}'.format(a,b, a*b, result)
    print '{:>5}  * {:>5}  = {:>10}       {}'.format(a,b, result._int, number.counts)
