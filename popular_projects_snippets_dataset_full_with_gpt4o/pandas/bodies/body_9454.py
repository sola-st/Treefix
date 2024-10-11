# Extracted from ./data/repos/pandas/pandas/tests/arrays/timedeltas/test_reductions.py
tdi = pd.TimedeltaIndex(["0H", "3H", "NaT", "5H06m", "0H", "2H"])
arr = tdi._data

# manually verified result
expected = Timedelta(arr.dropna()._ndarray.mean())

result = arr.mean()
assert result == expected
result = arr.mean(skipna=False)
assert result is pd.NaT

result = arr.dropna().mean(skipna=False)
assert result == expected

result = arr.mean(axis=0)
assert result == expected
