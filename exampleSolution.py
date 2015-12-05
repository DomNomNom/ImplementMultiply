from number import Integer

def multiply(a, b):

    # ensure b is positive
    if b < 0:
        a = -a
        b = -b

    # add A together B times
    # note: bitshifting could save us a lot of time
    i = Integer(0)
    result = Integer(0)
    while i < b:
        result += a
        i += 1

    return result


if __name__ == '__main__':
    import main
