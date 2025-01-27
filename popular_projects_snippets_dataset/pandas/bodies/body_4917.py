# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
obj = Index(np.arange(5, dtype="int64"))
assert obj.argmin() == 0
assert obj.argmax() == 4

obj = Index([np.nan, 1, np.nan, 2])
assert obj.argmin() == 1
assert obj.argmax() == 3
assert obj.argmin(skipna=False) == -1
assert obj.argmax(skipna=False) == -1

obj = Index([np.nan])
assert obj.argmin() == -1
assert obj.argmax() == -1
assert obj.argmin(skipna=False) == -1
assert obj.argmax(skipna=False) == -1

obj = Index([NaT, datetime(2011, 11, 1), datetime(2011, 11, 2), NaT])
assert obj.argmin() == 1
assert obj.argmax() == 2
assert obj.argmin(skipna=False) == -1
assert obj.argmax(skipna=False) == -1

obj = Index([NaT])
assert obj.argmin() == -1
assert obj.argmax() == -1
assert obj.argmin(skipna=False) == -1
assert obj.argmax(skipna=False) == -1
