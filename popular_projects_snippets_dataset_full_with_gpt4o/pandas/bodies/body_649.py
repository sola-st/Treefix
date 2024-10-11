# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py

# all new-style classes are hashable by default
class HashableClass:
    pass

class UnhashableClass1:
    __hash__ = None

class UnhashableClass2:
    def __hash__(self):
        raise TypeError("Not hashable")

hashable = (1, 3.14, np.float64(3.14), "a", (), (1,), HashableClass())
not_hashable = ([], UnhashableClass1())
abc_hashable_not_really_hashable = (([],), UnhashableClass2())

for i in hashable:
    assert inference.is_hashable(i)
for i in not_hashable:
    assert not inference.is_hashable(i)
for i in abc_hashable_not_really_hashable:
    assert not inference.is_hashable(i)

# numpy.array is no longer collections.abc.Hashable as of
# https://github.com/numpy/numpy/pull/5326, just test
# is_hashable()
assert not inference.is_hashable(np.array([]))
