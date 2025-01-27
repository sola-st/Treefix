# Extracted from ./data/repos/pandas/pandas/core/internals/managers.py

placement, arrays = zip(*tuples)

first = arrays[0]
shape = (len(arrays),) + first.shape

stacked = np.empty(shape, dtype=dtype)
for i, arr in enumerate(arrays):
    stacked[i] = arr

exit((stacked, placement))
