# Extracted from ./data/repos/pandas/pandas/tests/series/test_reductions.py
# GH#37151
ser = Series([], dtype="timedelta64[ns]")

result = ser.sum(skipna=skipna)
assert isinstance(result, pd.Timedelta)
assert result == pd.Timedelta(0)
