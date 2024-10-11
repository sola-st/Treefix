# Extracted from ./data/repos/pandas/pandas/tests/resample/test_datetime_index.py
s = series
s.index = s.index.as_unit(unit)

grouper = Grouper(freq=Minute(5))
expect = s.groupby(grouper).agg(lambda x: x[-1])
result = s.resample("5Min").ohlc()

assert len(result) == len(expect)
assert len(result.columns) == 4

xs = result.iloc[-2]
assert xs["open"] == s[-6]
assert xs["high"] == s[-6:-1].max()
assert xs["low"] == s[-6:-1].min()
assert xs["close"] == s[-2]

xs = result.iloc[0]
assert xs["open"] == s[0]
assert xs["high"] == s[:5].max()
assert xs["low"] == s[:5].min()
assert xs["close"] == s[4]
