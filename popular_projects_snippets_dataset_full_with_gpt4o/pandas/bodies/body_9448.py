# Extracted from ./data/repos/pandas/pandas/tests/arrays/timedeltas/test_reductions.py
arr = TimedeltaArray._from_sequence(["3H", "3H", "NaT", "2H", "5H", "4H"])

result = arr.min()
expected = Timedelta("2H")
assert result == expected

result = arr.max()
expected = Timedelta("5H")
assert result == expected

result = arr.min(skipna=False)
assert result is pd.NaT

result = arr.max(skipna=False)
assert result is pd.NaT
