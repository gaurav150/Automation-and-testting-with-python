def display(n):
    for i in range(n):
        if i == (n-1) or i == 0 or i == n // 2:
            print('*' * n)
        else:
            print('*')


display(9)