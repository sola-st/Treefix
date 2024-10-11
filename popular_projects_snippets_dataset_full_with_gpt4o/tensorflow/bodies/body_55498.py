# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util.py
exit(np.asarray(
    x, dtype=dtypes.float8_e4m3fn.as_numpy_dtype).view(np.uint8).item())
