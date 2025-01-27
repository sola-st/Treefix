# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_quantile.py
df = DataFrame({"a": pd.to_datetime(["2010", "2011"]), "b": [0, 5]})

# exclude datetime
result = df.quantile(0.5, numeric_only=True)
expected = Series([2.5], index=["b"], name=0.5)
tm.assert_series_equal(result, expected)

# datetime
result = df.quantile(0.5, numeric_only=False)
expected = Series(
    [Timestamp("2010-07-02 12:00:00"), 2.5], index=["a", "b"], name=0.5
)
tm.assert_series_equal(result, expected)

# datetime w/ multi
result = df.quantile([0.5], numeric_only=False)
expected = DataFrame(
    [[Timestamp("2010-07-02 12:00:00"), 2.5]], index=[0.5], columns=["a", "b"]
)
tm.assert_frame_equal(result, expected)

# axis = 1
df["c"] = pd.to_datetime(["2011", "2012"])
result = df[["a", "c"]].quantile(0.5, axis=1, numeric_only=False)
expected = Series(
    [Timestamp("2010-07-02 12:00:00"), Timestamp("2011-07-02 12:00:00")],
    index=[0, 1],
    name=0.5,
)
tm.assert_series_equal(result, expected)

result = df[["a", "c"]].quantile([0.5], axis=1, numeric_only=False)
expected = DataFrame(
    [[Timestamp("2010-07-02 12:00:00"), Timestamp("2011-07-02 12:00:00")]],
    index=[0.5],
    columns=[0, 1],
)
tm.assert_frame_equal(result, expected)

# empty when numeric_only=True
result = df[["a", "c"]].quantile(0.5, numeric_only=True)
expected = Series([], index=[], dtype=np.float64, name=0.5)
tm.assert_series_equal(result, expected)

result = df[["a", "c"]].quantile([0.5], numeric_only=True)
expected = DataFrame(index=[0.5], columns=[])
tm.assert_frame_equal(result, expected)
