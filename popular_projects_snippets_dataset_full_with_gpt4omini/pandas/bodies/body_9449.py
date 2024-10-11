# Extracted from ./data/repos/pandas/pandas/tests/arrays/timedeltas/test_reductions.py
tdi = pd.TimedeltaIndex(["3H", "3H", "NaT", "2H", "5H", "4H"])
arr = tdi.array

result = arr.sum(skipna=True)
expected = Timedelta(hours=17)
assert isinstance(result, Timedelta)
assert result == expected

result = tdi.sum(skipna=True)
assert isinstance(result, Timedelta)
assert result == expected

result = arr.sum(skipna=False)
assert result is pd.NaT

result = tdi.sum(skipna=False)
assert result is pd.NaT

result = arr.sum(min_count=9)
assert result is pd.NaT

result = tdi.sum(min_count=9)
assert result is pd.NaT

result = arr.sum(min_count=1)
assert isinstance(result, Timedelta)
assert result == expected

result = tdi.sum(min_count=1)
assert isinstance(result, Timedelta)
assert result == expected
