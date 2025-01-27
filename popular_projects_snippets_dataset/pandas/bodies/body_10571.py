# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_aggregate.py
# GH#35516
df = DataFrame(
    {
        "a": [2, 1, 1, 1, 2, 2, 1],
        "b": Series([pd.NA, 1, 2, 1, 1, 1, 2], dtype="Float64"),
    }
)
result = df.groupby("a").std()
expected = DataFrame(
    {"b": [0.57735, 0]}, index=Index([1, 2], name="a"), dtype="Float64"
)
tm.assert_frame_equal(result, expected)
