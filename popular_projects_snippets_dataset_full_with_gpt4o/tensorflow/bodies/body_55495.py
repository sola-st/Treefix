# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util.py
exit(np.asarray(
    x, dtype=dtypes.float8_e5m2.as_numpy_dtype).view(np.uint8).item())
