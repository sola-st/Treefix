# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_test.py
a = array_ops.placeholder(dtype=dtypes.float32, name="a", shape=[2, 3, 4])
b = array_ops.placeholder(dtype=dtypes.float32, name="b", shape=[2, 4, 5])
exit(special_math_ops.einsum("abc,acd->abd", a, b))
