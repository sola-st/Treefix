# Extracted from ./data/repos/pandas/pandas/tests/resample/test_period_index.py
ts = simple_period_range_series("1990", "1992", freq=f"A-{month}")
quar_ts = ts.resample(f"Q-{month}").ffill()

stamps = ts.to_timestamp("D", how="start")
qdates = period_range(
    ts.index[0].asfreq("D", "start"),
    ts.index[-1].asfreq("D", "end"),
    freq=f"Q-{month}",
)

expected = stamps.reindex(qdates.to_timestamp("D", "s"), method="ffill")
expected.index = qdates

tm.assert_series_equal(quar_ts, expected)
