# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH6173, various appends to an empty dataframe

data = [1, 2]
df = DataFrame(columns=["x", "y"])
df.index = df.index.astype(np.int64)
msg = (
    rf"None of \[NumericIndex\(\[0, 1\], dtype='{np.int_().dtype}'\)\] "
    r"are in the \[index\]"
)
with pytest.raises(KeyError, match=msg):
    df.loc[[0, 1], "x"] = data

msg = "|".join(
    [
        "cannot copy sequence with size 2 to array axis with dimension 0",
        r"could not broadcast input array from shape \(2,\) into shape \(0,\)",
        "Must have equal len keys and value when setting with an iterable",
    ]
)
with pytest.raises(ValueError, match=msg):
    df.loc[0:2, "x"] = data
