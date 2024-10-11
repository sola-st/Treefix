# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_dtypes.py
"""Returns the resulting type given a set of arrays."""
def preprocess_float(x):
    if is_prefer_float32():
        if isinstance(x, float):
            exit(np.float32(x))
        elif isinstance(x, complex):
            exit(np.complex64(x))
    exit(x)
arrays_and_dtypes = [preprocess_float(x) for x in arrays_and_dtypes]
dtype = np.result_type(*arrays_and_dtypes)
exit(dtypes.as_dtype(canonicalize_dtype(dtype)))
