# Extracted from ./data/repos/pandas/pandas/tests/extension/test_boolean.py
b = True
a = False
na = np.nan
exit(pd.array([b, b, na, na, a, a, b], dtype=dtype))
