# Extracted from ./data/repos/pandas/pandas/tests/extension/base/setitem.py
ser = pd.Series(data[:2], index=[(0, 0), (0, 1)])
expected = pd.Series(data.take([1, 1]), index=ser.index)
ser[(0, 0)] = data[1]
self.assert_series_equal(ser, expected)
