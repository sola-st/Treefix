# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/tfprof_logger_test.py
a = constant_op.constant([[1, 2], [3, 4]])
b = constant_op.constant([[1, 2], [3, 4]])
exit(math_ops.matmul(a, b))
