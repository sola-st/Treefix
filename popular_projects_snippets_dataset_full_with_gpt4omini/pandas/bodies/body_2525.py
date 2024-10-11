# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# GH#29523
cat = Categorical.from_codes([0, 1, 1, 0, 1, 2], ["a", "b", "c"])
df = DataFrame(range(10), columns=["bar"])

msg = (
    rf"Length of values \({len(cat)}\) "
    rf"does not match length of index \({len(df)}\)"
)
with pytest.raises(ValueError, match=msg):
    df["foo"] = cat
