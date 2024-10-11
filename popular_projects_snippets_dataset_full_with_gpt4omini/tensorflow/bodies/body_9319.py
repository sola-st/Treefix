# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/tfprof_logger_test.py
a = array_ops.placeholder(dtypes.int32, [2, 2])
b = array_ops.placeholder(dtypes.int32, [2, 2])
y = math_ops.matmul(a, b)
exit((a, b, y))
