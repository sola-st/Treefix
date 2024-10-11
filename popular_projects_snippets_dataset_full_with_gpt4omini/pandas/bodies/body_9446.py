# Extracted from ./data/repos/pandas/pandas/tests/arrays/timedeltas/test_reductions.py
tdi = pd.TimedeltaIndex([])
arr = tdi.array

result = getattr(tdi, name)(skipna=skipna)
assert result is pd.NaT

result = getattr(arr, name)(skipna=skipna)
assert result is pd.NaT
