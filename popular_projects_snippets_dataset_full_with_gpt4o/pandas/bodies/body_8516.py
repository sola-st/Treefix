# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_indexing.py
# GH#1062
index = DatetimeIndex(["1/3/2000"])
with pytest.raises(KeyError, match="2000"):
    index.get_loc("1/1/2000")
