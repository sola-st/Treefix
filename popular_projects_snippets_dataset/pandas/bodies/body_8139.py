# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
# with both 0 and a large-uint64, np.array will infer to float64
#  https://github.com/numpy/numpy/issues/19146
#  but a more accurate choice would be uint64
values = [0, np.iinfo(np.uint64).max]

result = ensure_index(values)
assert list(result) == values

expected = Index(values, dtype="uint64")
tm.assert_index_equal(result, expected)
