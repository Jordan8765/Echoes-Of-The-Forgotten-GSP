def map(op, values):
    result = []
    for value in values:
        result.append(op(value))
    return result


print(f'{map(lambda x: x * 2, [1, 2, 3, 4, 5])}')

print(f'{map(lambda f: (f - 32) * 5 / 9, [60.0, 80.0, 100.0])}')