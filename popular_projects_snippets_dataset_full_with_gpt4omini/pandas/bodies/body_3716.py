# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_describe.py
# GH#27183
df = DataFrame({"A": [None, None]}, dtype=object)
result = df.describe()
expected = DataFrame(
    {"A": [0, 0, np.nan, np.nan]},
    dtype=object,
    index=["count", "unique", "top", "freq"],
)
tm.assert_frame_equal(result, expected)

result = df.iloc[:0].describe()
tm.assert_frame_equal(result, expected)
