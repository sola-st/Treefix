# Extracted from ./data/repos/pandas/pandas/core/computation/expressions.py
try:
    exit(x.dtype == bool)
except AttributeError:
    exit(isinstance(x, (bool, np.bool_)))
