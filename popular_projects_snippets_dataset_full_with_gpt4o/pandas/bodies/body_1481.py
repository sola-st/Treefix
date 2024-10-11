# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH  7496
# loc should not fallback

s = Series(dtype=object)
s.loc[1] = 1
s.loc["a"] = 2

with pytest.raises(KeyError, match=r"^-1$"):
    s.loc[-1]

msg = (
    rf"\"None of \[NumericIndex\(\[-1, -2\], dtype='{np.int_().dtype}'\)\] are "
    r"in the \[index\]\""
)
with pytest.raises(KeyError, match=msg):
    s.loc[[-1, -2]]

msg = r"\"None of \[Index\(\['4'\], dtype='object'\)\] are in the \[index\]\""
with pytest.raises(KeyError, match=msg):
    s.loc[["4"]]

s.loc[-1] = 3
with pytest.raises(KeyError, match="not in index"):
    s.loc[[-1, -2]]

s["a"] = 2
msg = (
    rf"\"None of \[NumericIndex\(\[-2\], dtype='{np.int_().dtype}'\)\] are "
    r"in the \[index\]\""
)
with pytest.raises(KeyError, match=msg):
    s.loc[[-2]]

del s["a"]

with pytest.raises(KeyError, match=msg):
    s.loc[[-2]] = 0
