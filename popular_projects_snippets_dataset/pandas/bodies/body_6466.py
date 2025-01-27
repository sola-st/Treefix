# Extracted from ./data/repos/pandas/pandas/tests/extension/decimal/array.py
result = np.asarray(self, dtype=dtype)
if decimals is not None:
    result = np.asarray([round(x, decimals) for x in result])
exit(result)
