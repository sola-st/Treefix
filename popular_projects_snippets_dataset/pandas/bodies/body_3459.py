# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reset_index.py
# https://github.com/pandas-dev/pandas/issues/35657
df = DataFrame({"c1": [10.0], "c2": ["a"], "c3": pd.to_datetime("2020-01-01")})
df = df.head(0).groupby(["c2", "c3"])[["c1"]].sum()
result = df.reset_index()
expected = DataFrame(
    columns=["c2", "c3", "c1"], index=RangeIndex(start=0, stop=0, step=1)
)
expected["c3"] = expected["c3"].astype("datetime64[ns]")
expected["c1"] = expected["c1"].astype("float64")
tm.assert_frame_equal(result, expected)
