# Extracted from ./data/repos/pandas/pandas/tests/indexes/common.py
result = np.argsort(index)
expected = index.argsort()
tm.assert_numpy_array_equal(result, expected)

result = np.argsort(index, kind="mergesort")
expected = index.argsort(kind="mergesort")
tm.assert_numpy_array_equal(result, expected)

# these are the only two types that perform
# pandas compatibility input validation - the
# rest already perform separate (or no) such
# validation via their 'values' attribute as
# defined in pandas.core.indexes/base.py - they
# cannot be changed at the moment due to
# backwards compatibility concerns
if isinstance(index, (CategoricalIndex, RangeIndex)):
    msg = "the 'axis' parameter is not supported"
    with pytest.raises(ValueError, match=msg):
        np.argsort(index, axis=1)

    msg = "the 'order' parameter is not supported"
    with pytest.raises(ValueError, match=msg):
        np.argsort(index, order=("a", "b"))
