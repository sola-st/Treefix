# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_melt.py
# GH 17440
df = DataFrame({"foo": [0], "bar": [1]}, index=["first"])
result = melt(df, ignore_index=False)
expected = DataFrame(
    {"variable": ["foo", "bar"], "value": [0, 1]}, index=["first", "first"]
)
tm.assert_frame_equal(result, expected)
