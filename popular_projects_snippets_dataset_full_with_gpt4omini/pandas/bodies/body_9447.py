# Extracted from ./data/repos/pandas/pandas/tests/arrays/timedeltas/test_reductions.py
tdi = pd.TimedeltaIndex([])
arr = tdi.array

result = tdi.sum(skipna=skipna)
assert isinstance(result, Timedelta)
assert result == Timedelta(0)

result = arr.sum(skipna=skipna)
assert isinstance(result, Timedelta)
assert result == Timedelta(0)
