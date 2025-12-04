def eval_postfix(expression):
    stack = []
    tokens = expression.split()
    
    for token in tokens:
        if token in ['*', '/']:
            right = stack.pop()
            left = stack.pop()
            
            if token == '*':
                result = left * right
            elif token == '/':
                result = left / right
            
            stack.append(result)
        else:
            stack.append(int(token))
    
    return stack[0]


print(f'{eval_postfix("8 4 /") = }')

print(f'{eval_postfix("6 11 *") = }')

print(f'{eval_postfix("2 3 1 / * 9 *") = }')

print(f'{eval_postfix("3 2 11 9 * / * 2 /") = }')