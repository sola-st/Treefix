# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py

# GH 7432
df = DataFrame(
    {"bar": [1, 2, 3], "baz": ["d", "e", "f"]},
    index=Index(["a", "b", "c"], name="foo"),
)
ser = Series(
    ["g", "h", "i", "j"],
    index=Index(["a", "b", "c", "a"], name="foo"),
    name="fiz",
)
msg = "cannot reindex on an axis with duplicate labels"
with pytest.raises(ValueError, match=msg):
    df["newcol"] = ser

# GH 4107, more descriptive error message
df = DataFrame(np.random.randint(0, 2, (4, 4)), columns=["a", "b", "c", "d"])

msg = "Cannot set a DataFrame with multiple columns to the single column gr"
with pytest.raises(ValueError, match=msg):
    df["gr"] = df.groupby(["b", "c"]).count()
