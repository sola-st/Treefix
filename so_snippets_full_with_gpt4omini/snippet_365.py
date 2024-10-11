# Extracted from https://stackoverflow.com/questions/4435169/how-do-i-append-one-string-to-another-in-python
%%timeit
x = []
for i in range(100000000):  # xrange on Python 2.7
    x.append('a')
x = ''.join(x)

%%timeit
x = ''
for i in range(100000000):  # xrange on Python 2.7
    x += 'a'

