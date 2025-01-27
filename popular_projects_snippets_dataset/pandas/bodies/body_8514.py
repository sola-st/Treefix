# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_indexing.py
# GH#20464
index = DatetimeIndex(["1/3/2000", "NaT"])
assert index.get_loc(pd.NaT) == 1

assert index.get_loc(None) == 1

assert index.get_loc(np.nan) == 1

assert index.get_loc(pd.NA) == 1

assert index.get_loc(np.datetime64("NaT")) == 1

with pytest.raises(KeyError, match="NaT"):
    index.get_loc(np.timedelta64("NaT"))
