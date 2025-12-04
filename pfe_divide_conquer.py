def find_dc(values, to_find):

    if len(values) == 0:
        return False
    
    if len(values) == 1:
        return values[0] == to_find
    
    mid = len(values) // 2
    left_half = values[:mid]
    right_half = values[mid:]
    
    return find_dc(left_half, to_find) or find_dc(right_half, to_find)


if __name__ == '__main__':
    print(f'{find_dc([5], 5) = }')

    print(f'{find_dc([5], 1) = }')

    print(f'{find_dc([1,2,3,4,5], 7) = }')

    print(f'{find_dc([-1,4,2,10,-3,-5], -5) = }')

    print(f'{find_dc([-1,4,2,10,-3,-5], -1) = }')

    print(f'{find_dc([5,-3,3,-5], 0) = }')
