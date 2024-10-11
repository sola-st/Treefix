# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_melt.py
# GH 17440
index = pd.Index(["foo", "bar"], dtype="category", name="baz")
df = DataFrame({"x": [0, 1], "y": [2, 3]}, index=index)
result = melt(df, ignore_index=False)

expected_index = pd.Index(["foo", "bar"] * 2, dtype="category", name="baz")
expected = DataFrame(
    {"variable": ["x", "x", "y", "y"], "value": [0, 1, 2, 3]},
    index=expected_index,
)

tm.assert_frame_equal(result, expected)
