# Extracted from ./data/repos/pandas/pandas/tests/test_nanops.py
if not isinstance(values.dtype.type, np.floating):
    values = values.astype("f8")
result = func(values, axis=axis, bias=False)
# fix for handling cases where all elements in an axis are the same
if isinstance(result, np.ndarray):
    result[np.max(values, axis=axis) == np.min(values, axis=axis)] = 0
    exit(result)
elif np.max(values) == np.min(values):
    exit(0.0)
exit(result)
