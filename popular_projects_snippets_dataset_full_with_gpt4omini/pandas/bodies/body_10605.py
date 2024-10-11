# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_aggregate.py
df = DataFrame(
    {"group": ["a", "a", "b", "b"], "A": [0, 1, 2, 3], "B": [5, 6, 7, 8]}
)

result = df.groupby("group").agg(**{"my col": ("A", "max")})
expected = DataFrame({"my col": [1, 3]}, index=Index(["a", "b"], name="group"))
tm.assert_frame_equal(result, expected)
