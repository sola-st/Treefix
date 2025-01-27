# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reindex.py
# passing date to dt64 is deprecated; enforced in 2.0 to cast to object
arr = date_range("2016-01-01", periods=6).values.reshape(3, 2)
df = DataFrame(arr, columns=["A", "B"], index=range(3))

ts = df.iloc[0, 0]
fv = ts.date()

res = df.reindex(index=range(4), columns=["A", "B", "C"], fill_value=fv)

expected = DataFrame(
    {"A": df["A"].tolist() + [fv], "B": df["B"].tolist() + [fv], "C": [fv] * 4},
    dtype=object,
)
tm.assert_frame_equal(res, expected)

# only reindexing rows
res = df.reindex(index=range(4), fill_value=fv)
tm.assert_frame_equal(res, expected[["A", "B"]])

# same with a datetime-castable str
res = df.reindex(
    index=range(4), columns=["A", "B", "C"], fill_value="2016-01-01"
)
expected = DataFrame(
    {"A": df["A"].tolist() + [ts], "B": df["B"].tolist() + [ts], "C": [ts] * 4},
)
tm.assert_frame_equal(res, expected)
