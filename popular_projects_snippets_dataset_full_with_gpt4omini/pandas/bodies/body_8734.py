# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
tdi = TimedeltaIndex(["1 Day", "3 Hours"])
arr = TimedeltaArray(tdi)
asobj = arr.astype("O")
assert isinstance(asobj, np.ndarray)
assert asobj.dtype == "O"
assert list(asobj) == list(tdi)
