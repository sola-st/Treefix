# Extracted from https://stackoverflow.com/questions/2573135/python-progression-path-from-apprentice-to-guru
x = ['foo', [1,2,3], 10.4]
y = list(x) # or x[:]
y[0] = 'fooooooo'
y[1][0] = 4
print x
print y

