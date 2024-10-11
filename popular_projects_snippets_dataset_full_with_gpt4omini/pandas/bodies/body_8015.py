# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_index_new.py
# see GH#15187
data = [np.nan]
msg = "cannot convert"
with pytest.raises(ValueError, match=msg):
    Index(data, dtype=dtype)
