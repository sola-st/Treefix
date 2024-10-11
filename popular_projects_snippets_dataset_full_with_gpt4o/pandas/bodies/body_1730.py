# Extracted from ./data/repos/pandas/pandas/tests/resample/test_datetime_index.py
df = tm.makeTimeDataFrame()
df.index = df.index.as_unit(unit)
result = df.resample(freq).mean()
tm.assert_series_equal(result["A"], df["A"].resample(freq).mean())
