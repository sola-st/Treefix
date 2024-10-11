# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py

# GH3449
df = DataFrame(
    np.random.random((3, 3)), index=["a", "b", "c"], columns=["e", "f", "g"]
)

msg = (
    rf"\"None of \[NumericIndex\(\[1, 2\], dtype='{np.int_().dtype}'\)\] are "
    r"in the \[index\]\""
)
with pytest.raises(KeyError, match=msg):
    df.loc[[1, 2], [1, 2]]
