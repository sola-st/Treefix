# Extracted from ./data/repos/pandas/pandas/tests/window/test_groupby.py
# GH 13966 (similar to #15130, closed by #15175)

# superseded by 43909
# GH 46061: OK if the on is monotonic relative to each each group

dates = date_range(start="2016-01-01 09:30:00", periods=20, freq="s")
df = DataFrame(
    {
        "A": [1] * 20 + [2] * 12 + [3] * 8,
        "B": np.concatenate((dates, dates)),
        "C": np.arange(40),
    }
)

expected = (
    df.set_index("B").groupby("A").apply(lambda x: x.rolling("4s")["C"].mean())
)
result = df.groupby("A").rolling("4s", on="B").C.mean()
tm.assert_series_equal(result, expected)
