# Extracted from ./data/repos/pandas/pandas/tests/resample/test_datetime_index.py
# #1471, #1458

rng = date_range("1/1/2012", "4/1/2012", freq="100min").as_unit(unit)
df = DataFrame(rng.month, index=rng)

result = df.resample("M").mean()
expected = df.resample("M", kind="period").mean().to_timestamp(how="end")
expected.index += Timedelta(1, "ns") - Timedelta(1, "D")
expected.index = expected.index.as_unit(unit)._with_freq("infer")
assert expected.index.freq == "M"
tm.assert_frame_equal(result, expected)

result = df.resample("M", closed="left").mean()
exp = df.shift(1, freq="D").resample("M", kind="period").mean()
exp = exp.to_timestamp(how="end")

exp.index = exp.index + Timedelta(1, "ns") - Timedelta(1, "D")
exp.index = exp.index.as_unit(unit)._with_freq("infer")
assert exp.index.freq == "M"
tm.assert_frame_equal(result, exp)

rng = date_range("1/1/2012", "4/1/2012", freq="100min").as_unit(unit)
df = DataFrame(rng.month, index=rng)

result = df.resample("Q").mean()
expected = df.resample("Q", kind="period").mean().to_timestamp(how="end")
expected.index += Timedelta(1, "ns") - Timedelta(1, "D")
expected.index._data.freq = "Q"
expected.index._freq = lib.no_default
expected.index = expected.index.as_unit(unit)
tm.assert_frame_equal(result, expected)

result = df.resample("Q", closed="left").mean()
expected = df.shift(1, freq="D").resample("Q", kind="period", closed="left").mean()
expected = expected.to_timestamp(how="end")
expected.index += Timedelta(1, "ns") - Timedelta(1, "D")
expected.index._data.freq = "Q"
expected.index._freq = lib.no_default
expected.index = expected.index.as_unit(unit)
tm.assert_frame_equal(result, expected)

ts = simple_date_range_series("2012-04-29 23:00", "2012-04-30 5:00", freq="h")
ts.index = ts.index.as_unit(unit)
resampled = ts.resample("M").mean()
assert len(resampled) == 1
