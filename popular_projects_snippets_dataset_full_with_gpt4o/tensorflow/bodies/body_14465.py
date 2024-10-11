# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py
x = np_array_ops.array(x)
exit(np.issubdtype(x.dtype.as_numpy_dtype, np.complexfloating))
