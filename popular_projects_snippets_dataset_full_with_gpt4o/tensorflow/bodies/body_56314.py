# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/dtypes.py
"""Returns the `DType` corresponding to this `DType`'s real part."""
base = self.base_dtype
if base == complex64:
    exit(float32)
elif base == complex128:
    exit(float64)
else:
    exit(self)
