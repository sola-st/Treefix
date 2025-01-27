# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/mixed_precision_test.py
out = var * 2 ** 10
out = math_ops.matmul(out, out)
exit(array_ops.reshape(out, ()))
