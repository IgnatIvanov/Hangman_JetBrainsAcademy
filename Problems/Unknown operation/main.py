def solve():
    # Write your code here

    if hidden_operation('random_string') == 'random_string':
        print('or')
        print(hidden_operation(False))
    elif hidden_operation(False):
        print('not')
    else:
        print('and')
        print(hidden_operation(True))