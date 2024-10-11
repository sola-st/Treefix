# Extracted from ./data/repos/pandas/pandas/tests/arrays/timedeltas/test_reductions.py
# GH#25282, GH#25335 np.sum should return a Timedelta, not timedelta64
tdi = pd.TimedeltaIndex(["3H", "3H", "2H", "5H", "4H"])
arr = tdi.array

result = np.sum(tdi)
expected = Timedelta(hours=17)
assert isinstance(result, Timedelta)
assert result == expected

result = np.sum(arr)
assert isinstance(result, Timedelta)
assert result == expected
