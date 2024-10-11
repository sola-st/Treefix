# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_getitem.py
# GH#33462 we expect the same behavior for list/ndarray/Index/Series
ser = Series(["A", "B"])

key = Series(["C"], dtype=object)
key = box(key)

msg = r"None of \[Index\(\['C'\], dtype='object'\)\] are in the \[index\]"
with pytest.raises(KeyError, match=msg):
    ser[key]
