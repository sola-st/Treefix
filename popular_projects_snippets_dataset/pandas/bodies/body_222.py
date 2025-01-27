# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py

# GH 16405
# 'size' is a property of frame/series
# validate that this is working
# GH 39116 - expand to apply
df = DataFrame(
    {"A": [None, 2, 3], "B": [1.0, np.nan, 3.0], "C": ["foo", None, "bar"]}
)

# Function aggregate
result = getattr(df, how)({"A": "count"})
expected = Series({"A": 2})

tm.assert_series_equal(result, expected)

# Non-function aggregate
result = getattr(df, how)({"A": "size"})
expected = Series({"A": 3})

tm.assert_series_equal(result, expected)

# Mix function and non-function aggs
result1 = getattr(df, how)(["count", "size"])
result2 = getattr(df, how)(
    {"A": ["count", "size"], "B": ["count", "size"], "C": ["count", "size"]}
)
expected = DataFrame(
    {
        "A": {"count": 2, "size": 3},
        "B": {"count": 2, "size": 3},
        "C": {"count": 2, "size": 3},
    }
)

tm.assert_frame_equal(result1, result2, check_like=True)
tm.assert_frame_equal(result2, expected, check_like=True)

# Just functional string arg is same as calling df.arg()
result = getattr(df, how)("count")
expected = df.count()

tm.assert_series_equal(result, expected)
