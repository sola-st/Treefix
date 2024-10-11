# Extracted from ./data/repos/pandas/pandas/core/dtypes/concat.py
if x.ndim <= axis:
    exit(True)
exit(x.shape[axis] > 0)
