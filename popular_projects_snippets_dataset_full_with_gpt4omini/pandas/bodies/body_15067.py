# Extracted from ./data/repos/pandas/pandas/tests/base/test_transpose.py
msg = "the 'axes' parameter is not supported"
obj = index_or_series_obj
with pytest.raises(ValueError, match=msg):
    obj.transpose(1)
with pytest.raises(ValueError, match=msg):
    obj.transpose(axes=1)
