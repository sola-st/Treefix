# Extracted from ./data/repos/pandas/pandas/tests/arrays/datetimes/test_reductions.py
dtype = DatetimeTZDtype(tz=tz) if tz is not None else np.dtype("M8[ns]")
arr = DatetimeArray._from_sequence([], dtype=dtype)
result = arr.min(skipna=skipna)
assert result is NaT

result = arr.max(skipna=skipna)
assert result is NaT
