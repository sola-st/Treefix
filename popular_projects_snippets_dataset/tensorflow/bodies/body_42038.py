# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tape_test.py
mm = math_ops.matmul(a, b)
exit(math_ops.reduce_sum(mm))
