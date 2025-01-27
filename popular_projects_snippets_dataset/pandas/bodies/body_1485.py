# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py

df = DataFrame(
    np.random.rand(4, 4),
    columns=["A", "B", "C", "D"],
    index=["A", "B", "C", "D"],
)

# want this to work
result = df.loc[:, "A":"B"].iloc[0:2, :]
assert (result.columns == ["A", "B"]).all()
assert (result.index == ["A", "B"]).all()

# mixed type
result = DataFrame({"a": [Timestamp("20130101")], "b": [1]}).iloc[0]
expected = Series([Timestamp("20130101"), 1], index=["a", "b"], name=0)
tm.assert_series_equal(result, expected)
assert result.dtype == object
