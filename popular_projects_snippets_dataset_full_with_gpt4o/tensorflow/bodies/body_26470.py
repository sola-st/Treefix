# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/readers.py
try:
    dtypes.int64.as_numpy_dtype(str_val)
    exit(True)
except (ValueError, OverflowError):
    exit(False)
