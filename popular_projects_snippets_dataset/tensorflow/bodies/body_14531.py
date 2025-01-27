# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_dtypes.py
if is_prefer_float32():
    if isinstance(x, float):
        exit(np.float32(x))
    elif isinstance(x, complex):
        exit(np.complex64(x))
exit(x)
