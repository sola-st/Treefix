# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#35509
df = DataFrame(
    {"col1": ["a", "b", "c"], "col2": [1, 2, 3]},
    index=to_datetime(["2020-08-01", "2020-07-02", "2020-08-05"]),
)
expected = DataFrame(
    {"col1": ["a", "c"], "col2": [1, 3]},
    index=to_datetime(["2020-08-01", "2020-08-05"]),
)
result = df.loc["2020-08"]
tm.assert_frame_equal(result, expected)
