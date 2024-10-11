# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_range.py
# make sure that our len is the same as np.arange calc
start, stop = (0, 5) if step > 0 else (5, 0)

arr = np.arange(start, stop, step)
index = RangeIndex(start, stop, step)
assert len(index) == len(arr)

index = RangeIndex(stop, start, step)
assert len(index) == 0
