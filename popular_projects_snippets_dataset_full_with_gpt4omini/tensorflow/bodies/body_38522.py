# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_unary_test.py
y = np_func(x.astype(np.float32))
exit(y.astype(x.dtype))
