# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
if as_td:
    idx = pd.TimedeltaIndex(arr)
else:
    idx = DatetimeIndex(arr)
assert idx.dtype == arr.dtype
