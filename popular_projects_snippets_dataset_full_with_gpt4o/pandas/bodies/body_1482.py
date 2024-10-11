# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# inconsistency between .loc[values] and .loc[values,:]
# GH 7999
df = DataFrame([["a"], ["b"]], index=[1, 2], columns=["value"])

msg = (
    rf"\"None of \[NumericIndex\(\[3\], dtype='{np.int_().dtype}'\)\] are "
    r"in the \[index\]\""
)
with pytest.raises(KeyError, match=msg):
    df.loc[[3], :]

with pytest.raises(KeyError, match=msg):
    df.loc[[3]]
