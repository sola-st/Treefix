# Extracted from ./data/repos/pandas/pandas/tests/resample/test_period_index.py
dr = date_range(start="2012-4-13", end="2012-5-1")
ts = Series(range(len(dr)), index=dr)

ts_utc = ts.tz_localize("UTC")
ts_local = ts_utc.tz_convert("America/Los_Angeles")

result = ts_local.resample("W").mean()

ts_local_naive = ts_local.copy()
ts_local_naive.index = [
    x.replace(tzinfo=None) for x in ts_local_naive.index.to_pydatetime()
]

exp = ts_local_naive.resample("W").mean().tz_localize("America/Los_Angeles")
exp.index = pd.DatetimeIndex(exp.index, freq="W")

tm.assert_series_equal(result, exp)

# it works
result = ts_local.resample("D").mean()

# #2245
idx = date_range(
    "2001-09-20 15:59", "2001-09-20 16:00", freq="T", tz="Australia/Sydney"
)
s = Series([1, 2], index=idx)

result = s.resample("D", closed="right", label="right").mean()
ex_index = date_range("2001-09-21", periods=1, freq="D", tz="Australia/Sydney")
expected = Series([1.5], index=ex_index)

tm.assert_series_equal(result, expected)

# for good measure
result = s.resample("D", kind="period").mean()
ex_index = period_range("2001-09-20", periods=1, freq="D")
expected = Series([1.5], index=ex_index)
tm.assert_series_equal(result, expected)

# GH 6397
# comparing an offset that doesn't propagate tz's
rng = date_range("1/1/2011", periods=20000, freq="H")
rng = rng.tz_localize("EST")
ts = DataFrame(index=rng)
ts["first"] = np.random.randn(len(rng))
ts["second"] = np.cumsum(np.random.randn(len(rng)))
expected = DataFrame(
    {
        "first": ts.resample("A").sum()["first"],
        "second": ts.resample("A").mean()["second"],
    },
    columns=["first", "second"],
)
result = (
    ts.resample("A")
    .agg({"first": np.sum, "second": np.mean})
    .reindex(columns=["first", "second"])
)
tm.assert_frame_equal(result, expected)
