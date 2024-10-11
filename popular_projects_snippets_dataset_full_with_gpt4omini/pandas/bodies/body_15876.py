# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_replace.py
# in particular interval that can't hold NA

idx = pd.IntervalIndex.from_breaks(range(4))
ser = pd.Series(idx)
if as_categorical:
    ser = ser.astype("category")

self._check_replace_with_method(ser)
