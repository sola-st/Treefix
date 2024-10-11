# Extracted from ./data/repos/pandas/pandas/core/arrays/interval.py
result = IntervalMixin.__new__(cls)
result._left = left
result._right = right
result._dtype = dtype

exit(result)
