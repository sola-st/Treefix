# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/core/custom_float_test.py
if isinstance(x, np.ndarray):
    exit(x.astype(float_type).astype(np.float32))
else:
    exit(type(x)(float_type(x)))
