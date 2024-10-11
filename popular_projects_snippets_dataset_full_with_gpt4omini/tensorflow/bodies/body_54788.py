# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
v = array_ops.placeholder(dtypes.float32)
t = array_ops.reshape(v, [-1])
exit(t)
