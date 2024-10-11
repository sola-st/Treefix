# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util.py
exit(np.asarray(
    x, dtype=dtypes.bfloat16.as_numpy_dtype).view(np.uint16).item())
