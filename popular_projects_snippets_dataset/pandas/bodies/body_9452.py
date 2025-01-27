# Extracted from ./data/repos/pandas/pandas/tests/arrays/timedeltas/test_reductions.py
tdi = pd.TimedeltaIndex(["0H", "4H", "NaT", "4H", "0H", "2H"]) + add
arr = tdi.array

result = arr.std(skipna=True)
expected = Timedelta(hours=2)
assert isinstance(result, Timedelta)
assert result == expected

result = tdi.std(skipna=True)
assert isinstance(result, Timedelta)
assert result == expected

if getattr(arr, "tz", None) is None:
    result = nanops.nanstd(np.asarray(arr), skipna=True)
    assert isinstance(result, np.timedelta64)
    assert result == expected

result = arr.std(skipna=False)
assert result is pd.NaT

result = tdi.std(skipna=False)
assert result is pd.NaT

if getattr(arr, "tz", None) is None:
    result = nanops.nanstd(np.asarray(arr), skipna=False)
    assert isinstance(result, np.timedelta64)
    assert np.isnat(result)
