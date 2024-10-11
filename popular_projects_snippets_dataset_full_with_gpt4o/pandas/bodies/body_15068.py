# Extracted from ./data/repos/pandas/pandas/tests/base/test_transpose.py
msg = "the 'axes' parameter is not supported"
obj = index_or_series_obj
tm.assert_equal(np.transpose(obj), obj)

with pytest.raises(ValueError, match=msg):
    np.transpose(obj, axes=1)
