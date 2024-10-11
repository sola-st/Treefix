# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
# demonstration tests
df = DataFrame({"A": range(5), "B": 5})
result = df.agg({"A": ["min", "max"], "B": ["sum", "max"]})
expected = DataFrame(
    {"A": [4.0, 0.0, np.nan], "B": [5.0, np.nan, 25.0]},
    columns=["A", "B"],
    index=["max", "min", "sum"],
)
tm.assert_frame_equal(result.reindex_like(expected), expected)
