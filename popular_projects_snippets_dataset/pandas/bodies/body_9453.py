# Extracted from ./data/repos/pandas/pandas/tests/arrays/timedeltas/test_reductions.py
tdi = pd.TimedeltaIndex(["0H", "3H", "NaT", "5H06m", "0H", "2H"])
arr = tdi.array

result = arr.median(skipna=True)
expected = Timedelta(hours=2)
assert isinstance(result, Timedelta)
assert result == expected

result = tdi.median(skipna=True)
assert isinstance(result, Timedelta)
assert result == expected

result = arr.median(skipna=False)
assert result is pd.NaT

result = tdi.median(skipna=False)
assert result is pd.NaT
