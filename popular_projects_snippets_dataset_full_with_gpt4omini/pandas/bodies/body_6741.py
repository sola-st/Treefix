# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_astype.py
index = interval_range(0.0, 10.0)
dtype = IntervalDtype(subtype, "right")
result = index.astype(dtype)
expected = IntervalIndex.from_arrays(
    index.left.astype(subtype), index.right.astype(subtype), closed=index.closed
)
tm.assert_index_equal(result, expected)

# raises with NA
msg = r"Cannot convert non-finite values \(NA or inf\) to integer"
with pytest.raises(ValueError, match=msg):
    index.insert(0, np.nan).astype(dtype)
