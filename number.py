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
    '''Acts like a int but counts the Integer of operations done'''
    def __init__(self, num):
        self._int = getInt(num)

    def __repr__(self):
        return '({})'.format(self._int)

    def __neg__      (self):        counts['negation'  ] += 1;  return Integer(-self._int)
    def __eq__       (self, other): counts['comparison'] += 1;  return self._int == getInt(other)
    def __lt__       (self, other): counts['comparison'] += 1;  return self._int < getInt(other)
    def __nonzero__  (self, other): counts['comparison'] += 1;  return bool(self._int)

    # def __add__(self, other): return makeFunctionality('add')(self, other)
    def __add__      (self, other): return makeFunctionality('add'      )(self, other)
    def __div__      (self, other): return makeFunctionality('div'      )(self, other)
    def __divmod__   (self, other): return makeFunctionality('divmod'   )(self, other)
    def __floordiv__ (self, other): return makeFunctionality('floordiv' )(self, other)
    def __lshift__   (self, other): return makeFunctionality('lshift'   )(self, other)
    def __mod__      (self, other): return makeFunctionality('mod'      )(self, other)
    def __rshift__   (self, other): return makeFunctionality('rshift'   )(self, other)
    def __sub__      (self, other): return makeFunctionality('sub'      )(self, other)
    def __radd__     (self, other): return makeFunctionality('add',      '__radd__'      )(self, other)
    def __rdiv__     (self, other): return makeFunctionality('div',      '__rdiv__'      )(self, other)
    def __rdivmod__  (self, other): return makeFunctionality('divmod',   '__rdivmod__'   )(self, other)
    def __rfloordiv__(self, other): return makeFunctionality('floordiv', '__rfloordiv__' )(self, other)
    def __rlshift__  (self, other): return makeFunctionality('lshift',   '__rlshift__'   )(self, other)
    def __rmod__     (self, other): return makeFunctionality('mod',      '__rmod__'      )(self, other)
    def __rrshift__  (self, other): return makeFunctionality('rshift',   '__rrshift__'   )(self, other)
    def __rsub__     (self, other): return makeFunctionality('sub',      '__rsub__'      )(self, other)


if __name__ == '__main__':
    import main
