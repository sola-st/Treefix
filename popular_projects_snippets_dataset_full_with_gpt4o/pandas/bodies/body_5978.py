# Extracted from ./data/repos/pandas/pandas/tests/extension/test_integer.py
b = 1
a = 0
c = 2
na = pd.NA
exit(pd.array([b, b, na, na, a, a, b, c], dtype=dtype))
