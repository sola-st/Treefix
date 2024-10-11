# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_setops.py
if isinstance(index, MultiIndex):
    index = index.rename(list(range(index.nlevels)))
else:
    index = index.rename("foo")

other = np.asarray(index)

result = index.intersection(other)
assert result.name == index.name

# empty other, same dtype
result = index.intersection(other[:0])
assert result.name == index.name

# empty `self`
result = index[:0].intersection(other)
assert result.name == index.name
