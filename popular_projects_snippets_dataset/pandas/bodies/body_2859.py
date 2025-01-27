# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_fillna.py
# GH#7095
df = DataFrame(
    {
        "A": [-1, -2, np.nan],
        "B": date_range("20130101", periods=3),
        "C": ["foo", "bar", None],
        "D": ["foo2", "bar2", None],
    },
    index=date_range("20130110", periods=3),
)
result = df.fillna("?")
expected = DataFrame(
    {
        "A": [-1, -2, "?"],
        "B": date_range("20130101", periods=3),
        "C": ["foo", "bar", "?"],
        "D": ["foo2", "bar2", "?"],
    },
    index=date_range("20130110", periods=3),
)
tm.assert_frame_equal(result, expected)

df = DataFrame(
    {
        "A": [-1, -2, np.nan],
        "B": [Timestamp("2013-01-01"), Timestamp("2013-01-02"), NaT],
        "C": ["foo", "bar", None],
        "D": ["foo2", "bar2", None],
    },
    index=date_range("20130110", periods=3),
)
result = df.fillna("?")
expected = DataFrame(
    {
        "A": [-1, -2, "?"],
        "B": [Timestamp("2013-01-01"), Timestamp("2013-01-02"), "?"],
        "C": ["foo", "bar", "?"],
        "D": ["foo2", "bar2", "?"],
    },
    index=date_range("20130110", periods=3),
)
tm.assert_frame_equal(result, expected)
