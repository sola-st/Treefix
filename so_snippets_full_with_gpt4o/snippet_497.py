# Extracted from https://stackoverflow.com/questions/28663856/how-do-i-count-the-occurrence-of-a-certain-item-in-an-ndarray
y = np.array([0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1])

np.sum(y)

np.count_nonzero(y)

import collections
collections.Counter(y)
> Counter({0: 8, 1: 4})

collections.Counter(y)[0]
> 8

