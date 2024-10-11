# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_generic.py
# GH7175 - GOTCHA: You can't use dot notation to add a column...
d = {
    "one": pd.Series([1.0, 2.0, 3.0], index=["a", "b", "c"]),
    "two": pd.Series([1.0, 2.0, 3.0, 4.0], index=["a", "b", "c", "d"]),
}
df = pd.DataFrame(d)

with catch_warnings(record=True) as w:
    #  successfully add new column
    #  this should not raise a warning
    df["three"] = df.two + 1
    assert len(w) == 0
    assert df.three.sum() > df.two.sum()

with catch_warnings(record=True) as w:
    #  successfully modify column in place
    #  this should not raise a warning
    df.one += 1
    assert len(w) == 0
    assert df.one.iloc[0] == 2

with catch_warnings(record=True) as w:
    #  successfully add an attribute to a series
    #  this should not raise a warning
    df.two.not_an_index = [1, 2]
    assert len(w) == 0

with tm.assert_produces_warning(UserWarning):
    #  warn when setting column to nonexistent name
    df.four = df.two + 2
    assert df.four.sum() > df.two.sum()
