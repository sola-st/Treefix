# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_indexing.py
rng = timedelta_range("1 day 1 s", periods=5, freq="h")
ser = Series(rng)
assert isinstance(ser[0], Timedelta)
assert isinstance(ser.at[1], Timedelta)
assert isinstance(ser.iat[2], Timedelta)
assert isinstance(ser.loc[3], Timedelta)
assert isinstance(ser.iloc[4], Timedelta)
