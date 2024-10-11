# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_frame_equal.py
dtypes = (any_numeric_ea_dtype, "int64")
obj1 = frame_or_series([1, 2], dtype=dtypes[indexer[0]])
obj2 = frame_or_series([1, 2], dtype=dtypes[indexer[1]])
msg = r'(Series|DataFrame.iloc\[:, 0\] \(column name="0"\) classes) are different'
with pytest.raises(AssertionError, match=msg):
    tm.assert_equal(obj1, obj2, check_exact=True, check_dtype=False)
