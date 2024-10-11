# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH 27395, non-ns dtype assignment via .loc should work
# and return the same result when using simple assignment
df = DataFrame(
    {
        "timestamp": [
            np.datetime64("2017-02-11 12:41:29"),
            np.datetime64("1991-11-07 04:22:37"),
        ]
    }
)

df.loc[:, unit] = df.loc[:, "timestamp"].values.astype(f"datetime64[{unit}]")
df["expected"] = df.loc[:, "timestamp"].values.astype(f"datetime64[{unit}]")
expected = Series(df.loc[:, "expected"], name=unit)
tm.assert_series_equal(df.loc[:, unit], expected)
