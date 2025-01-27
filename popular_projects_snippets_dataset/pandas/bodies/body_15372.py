# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
ser = Series(tm.rands_array(5, 10), index=tm.rands_array(10, 10))

msg = "index -11 is out of bounds for axis 0 with size 10"
with pytest.raises(IndexError, match=msg):
    ser[-11] = "foo"
