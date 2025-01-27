# Extracted from ./data/repos/pandas/pandas/tests/extension/base/setitem.py
# GH#40763
ser = pd.Series(data, name="data")

taker = np.arange(len(ser))
taker = np.delete(taker, 1)

expected = ser[taker]
del ser[1]
self.assert_series_equal(ser, expected)
