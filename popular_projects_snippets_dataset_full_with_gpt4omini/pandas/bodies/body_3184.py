# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_asof.py
N = 10
# explicitly cast to float to avoid implicit upcast when setting to np.nan
df = date_range_frame.iloc[:N].copy().astype({"A": "float"})
df.loc[df.index[4:8], "A"] = np.nan
dates = date_range("1/1/1990", periods=N * 3, freq="25s")

# with a subset of A should be the same
result = df.asof(dates, subset="A")
expected = df.asof(dates)
tm.assert_frame_equal(result, expected)

# same with A/B
result = df.asof(dates, subset=["A", "B"])
expected = df.asof(dates)
tm.assert_frame_equal(result, expected)

# B gives df.asof
result = df.asof(dates, subset="B")
expected = df.resample("25s", closed="right").ffill().reindex(dates)
expected.iloc[20:] = 9
# no "missing", so "B" can retain int dtype (df["A"].dtype platform-dependent)
expected["B"] = expected["B"].astype(df["B"].dtype)

tm.assert_frame_equal(result, expected)
