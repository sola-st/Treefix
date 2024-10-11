# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_getitem.py
# don't segfault, GH#495
msg = r"index \d+ is out of bounds for axis 0 with size \d+"
with pytest.raises(IndexError, match=msg):
    datetime_series[len(datetime_series)]
