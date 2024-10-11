# Extracted from ./data/repos/pandas/pandas/tests/extension/test_floating.py
b = 0.1
a = 0.0
c = 0.2
na = pd.NA
exit(pd.array([b, b, na, na, a, a, b, c], dtype=dtype))
