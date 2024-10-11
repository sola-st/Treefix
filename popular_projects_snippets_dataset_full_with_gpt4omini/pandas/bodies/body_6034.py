# Extracted from ./data/repos/pandas/pandas/tests/extension/test_numpy.py
ser = pd.Series(data)
self._check_divmod_op(ser, divmod, data, exc=None)
