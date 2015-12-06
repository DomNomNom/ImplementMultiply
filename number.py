from collections import Counter

counts = Counter()  # counts the operations that have been done


# returns the internal integer for a given Integer but also handles plain integers
def getInt(num):
    if type(num) == int:
        return num
    elif type(num) == Integer:
        return num._int
    else:
        assert False, 'argument is not a valid Integer (has to be int or Integer): ' + repr(num)

# creates a wrapper for a operator which when called also increases the counter
def makeFunctionality(niceName, funcName=None):
    if funcName is None:
        funcName = '__{}__'.format(niceName)

    def wrapper(self, other):
        counts[niceName] += 1
        # print 'running twoArgFunction: {}({}, {})'.format(niceName, self, other)
        return Integer(self._int.__getattribute__(funcName)(getInt(other)))
    return wrapper


class Integer(object):
    '''Acts like an int but counts the operations that are applied'''
    def __init__(self, num):
        self._int = getInt(num)

    def __repr__(self):
        # return '({})'.format(self._int)
        return str(self._int)

    # comparison
    def __nonzero__  (self): counts['comparison'] += 1;  return bool(getInt(self))
    def __eq__       (self, other): counts['comparison'] += 1;  return getInt(self) == getInt(other)
    def __lt__       (self, other): counts['comparison'] += 1;  return getInt(self) <  getInt(other)
    def __le__       (self, other): counts['comparison'] += 1;  return getInt(self) <= getInt(other)
    def __gt__       (self, other): counts['comparison'] += 1;  return getInt(self) >  getInt(other)
    def __ge__       (self, other): counts['comparison'] += 1;  return getInt(self) >= getInt(other)

    # divmod(a, b)
    def __divmod__   (self, other): counts['divmod'] += 1;  return tuple(map(Integer, divmod(getInt(self), getInt(other))))
    def __rdivmod__  (self, other): counts['divmod'] += 1;  return tuple(map(Integer, divmod(getInt(other), getInt(self))))

    # a bunch of common math operations
    def __add__      (self, other): return makeFunctionality('add'      )(self, other)
    def __div__      (self, other): return makeFunctionality('div'      )(self, other)
    def __floordiv__ (self, other): return makeFunctionality('floordiv' )(self, other)
    def __mod__      (self, other): return makeFunctionality('mod'      )(self, other)
    def __sub__      (self, other): return makeFunctionality('sub'      )(self, other)
    def __radd__     (self, other): return makeFunctionality('add',      '__radd__'      )(self, other)
    def __rdiv__     (self, other): return makeFunctionality('div',      '__rdiv__'      )(self, other)
    def __rfloordiv__(self, other): return makeFunctionality('floordiv', '__rfloordiv__' )(self, other)
    def __rmod__     (self, other): return makeFunctionality('mod',      '__rmod__'      )(self, other)
    def __rsub__     (self, other): return makeFunctionality('sub',      '__rsub__'      )(self, other)

    # note: these call other operators
    def __neg__(self): return 0 - self
    def __abs__(self): return self if self >= 0 else -self

    # bit shifting
    def __rshift__   (self, other): return makeFunctionality('rshift'   )(self, other)
    def __lshift__   (self, other): return makeFunctionality('lshift'   )(self, other)
    def __rrshift__  (self, other): return makeFunctionality('rshift',   '__rrshift__'   )(self, other)
    def __rlshift__  (self, other): return makeFunctionality('lshift',   '__rlshift__'   )(self, other)

    # excluded operators: mult, pow and any other bitwise operators


def tests():
    z = Integer(0)
    assert z == 0
    assert z <= 0
    assert z >= 0
    assert -1 < z < 1
    assert z + z == z
    assert         2  +         3    == 5
    assert Integer(2) +         3    == 5
    assert Integer(2) + Integer(3)   == 5
    assert         2  + Integer(3)   == 5
    assert         2  + Integer(3)   == Integer(5)
    assert         2  +         3    == Integer(5)
    assert sum([   2,   Integer(3)]) == 5

    # assert integer division
    assert Integer(3) /  2 == 1
    assert Integer(3) // 2 == 1

    assert divmod(7, Integer(5))          == (7 / 5, 7 % Integer(5))
    assert divmod(Integer(7), Integer(5)) == (7 / 5, 7 % Integer(5))

    assert bool(z) is False
    assert bool(Integer(-2)) is True

    assert abs(Integer( 3)) == 3
    assert abs(Integer(-3)) == 3

tests()

if __name__ == '__main__':
    import main
