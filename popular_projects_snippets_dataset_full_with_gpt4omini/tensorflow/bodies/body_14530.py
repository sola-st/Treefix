# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_dtypes.py
if not _allow_float64:
    try:
        exit(_to_float32[dtype])
    except KeyError:
        pass
exit(dtype)
