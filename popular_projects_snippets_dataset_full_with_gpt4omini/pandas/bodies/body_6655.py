# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_constructors.py
result = RangeIndex(*args, name=name, **kwargs)
expected = Index(np.arange(start, stop, step, dtype=np.int64), name=name)
assert isinstance(result, RangeIndex)
assert result.name is name
assert result._range == range(start, stop, step)
tm.assert_index_equal(result, expected, exact="equiv")
