# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_index_new.py
# see GH#15832
msg = (
    "The elements provided in the data cannot "
    "all be casted to the dtype int64"
)
with pytest.raises(OverflowError, match=msg):
    Index([np.iinfo(np.uint64).max - 1], dtype="int64")
