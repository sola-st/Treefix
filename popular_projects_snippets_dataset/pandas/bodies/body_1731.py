# Extracted from ./data/repos/pandas/pandas/tests/resample/test_datetime_index.py
df = tm.makeTimeDataFrame()
df.index = df.index.as_unit(unit)
df.resample(freq, kind="period").mean()
