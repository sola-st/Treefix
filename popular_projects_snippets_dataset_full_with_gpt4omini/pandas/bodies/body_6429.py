# Extracted from ./data/repos/pandas/pandas/tests/extension/test_interval.py
a = (0, 1)
b = (1, 2)
c = (2, 3)
exit(IntervalArray.from_tuples([b, b, None, None, a, a, b, c]))
