a = 5
b = 2*a-2
for c in range(0, a):
    for d in range(0, b):
        print(' ', end='')
    b -= 2
    for d in range(0, c + 1):
        print('* ', end='')
    print('')
