# Extracted from ./data/repos/pandas/pandas/compat/numpy/function.py
if isinstance(skipna, ndarray) or skipna is None:
    args = (skipna,) + args
    skipna = True

exit((skipna, args))
