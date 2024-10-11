# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
index = pd.timedelta_range("1 days", periods=5)
index = index._with_freq(None)  # won't be preserved by constructors
dtype = index.dtype

values = getattr(index, attr)

result = klass(values, dtype=dtype)
tm.assert_index_equal(result, index)

result = klass(list(values), dtype=dtype)
tm.assert_index_equal(result, index)
