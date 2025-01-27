# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_array.py
cumsum = np.cumsum if numpy else lambda s: s.cumsum()

out = cumsum(SparseArray(data))
tm.assert_sp_array_equal(out, expected)

out = cumsum(SparseArray(data, fill_value=np.nan))
tm.assert_sp_array_equal(out, expected)

out = cumsum(SparseArray(data, fill_value=2))
tm.assert_sp_array_equal(out, expected)

if numpy:  # numpy compatibility checks.
    msg = "the 'dtype' parameter is not supported"
    with pytest.raises(ValueError, match=msg):
        np.cumsum(SparseArray(data), dtype=np.int64)

    msg = "the 'out' parameter is not supported"
    with pytest.raises(ValueError, match=msg):
        np.cumsum(SparseArray(data), out=out)
else:
    axis = 1  # SparseArray currently 1-D, so only axis = 0 is valid.
    msg = re.escape(f"axis(={axis}) out of bounds")
    with pytest.raises(ValueError, match=msg):
        SparseArray(data).cumsum(axis=axis)
