def map(op, values):
    result = []
    for value in values:
        result.append(op(value))
    return result


def filter(op, values):
    result = []
    for value in values:
        if op(value):
            result.append(value)
    return result


def reduce(op, values):
    result = values[0]
    for i in range(1, len(values)):
        result = op(result, values[i])
    return result


print(f'{map(lambda x: x * 2, [1, 2, 3, 4, 5])}')

print(f'{map(lambda f: (f - 32) * 5 / 9, [60.0, 80.0, 100.0])}')

print(f'{filter(lambda x: x > 80.0, [64.5, 87.0, 55.5, 94.0, 71.5, 46.0, 100.0])}')

print(f'{filter(lambda x: (x % 2) == 0, [1,2,3,4,5,6])}')

print(f'{reduce(lambda x,y: x + y, [1,2,3,4,5])}')

print(f'{reduce(lambda x,y: x * y, [1,2,3,4,5])}')