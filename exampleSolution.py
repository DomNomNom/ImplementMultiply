from number import Integer

def multiply(a, b):
    i = Integer(0)
    result = Integer(0)

    if b < 0:
        a = -a
        b = -b

    while i < b:
        result += a
        i = 1 + i

    return result


if __name__ == '__main__':
    import main
