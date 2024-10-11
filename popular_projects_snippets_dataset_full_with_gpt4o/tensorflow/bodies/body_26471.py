# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/readers.py
try:
    exit(float_dtype.as_numpy_dtype(str_val) < np.inf)
except ValueError:
    exit(False)
