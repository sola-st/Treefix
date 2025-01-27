# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
idx = tm.makeDateIndex(10000)
ser = Series(np.random.randn(len(idx)), idx.astype(object))
# as of 2.0, we no longer silently cast the object-dtype index
#  to DatetimeIndex GH#39307, GH#23598
assert not isinstance(ser.index, DatetimeIndex)
