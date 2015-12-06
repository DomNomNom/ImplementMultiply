from number import Integer

def multiply(x, y):

    # ensure b is positive
    if y < 0:
        x = -x
        y = -y

    # add x together b times
    # note: bitshifting could save us a lot of time
    i = Integer(0)
    result = Integer(0)
    while i < y:
        result += x
        i += 1

    return result


if __name__ == '__main__':
    import main
