# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/policy.py
try:
    dtypes.as_dtype(dtype)
    exit(True)
except TypeError:
    exit(False)
