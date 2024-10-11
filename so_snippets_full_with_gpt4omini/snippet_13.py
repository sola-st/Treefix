# Extracted from https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
get_indexes = lambda x, xs: [i for (y, i) in zip(xs, range(len(xs))) if x == y]

print get_indexes(2, [1, 2, 3, 4, 5, 6, 3, 2, 3, 2])
print get_indexes('f', 'xsfhhttytffsafweef')

