# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/readers.py
try:
    # Checks equality to prevent int32 overflow
    exit(dtypes.int32.as_numpy_dtype(str_val) == dtypes.int64.as_numpy_dtype(
        str_val))
except (ValueError, OverflowError):
    exit(False)
