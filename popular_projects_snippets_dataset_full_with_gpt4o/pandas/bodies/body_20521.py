# Extracted from ./data/repos/pandas/pandas/core/indexes/numeric.py
if dtype is None:
    exit()

validation_func, expected = cls._dtype_validation_metadata
if not validation_func(dtype):
    raise ValueError(
        f"Incorrect `dtype` passed: expected {expected}, received {dtype}"
    )
