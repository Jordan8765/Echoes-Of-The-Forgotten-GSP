def make_change_greedy(amount_owed, denominations):
    
    change = []
    for denom in denominations:
        while amount_owed >= denom:
            change.append(denom)
            amount_owed -= denom
    return change

# Test cases
print(f'{make_change_greedy(17, [20, 10, 5, 2, 1]) = }')
print(f'{make_change_greedy(33, [20, 10, 5, 2, 1]) = }')
print(f'{make_change_greedy(78, [20, 10, 5, 2, 1]) = }')
