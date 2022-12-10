def fizzbuzz(x):
    if x is None:
        raise TypeError('num cannot be None')
    if x < 1:
        raise ValueError('num cannot be less than one')
    for i in range(1, x):
        output = i
        if i % 3 == 0:
            output = 'fizz'
        if i % 5 == 0:
            if output == i:
                output = ''
            output += 'buzz'
        print(output)

