# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
constant_two = constant_op.constant(2, dtypes.int32)
two_on_gpu = math_ops.cast(constant_two, dtypes.float32)
exit(x * two_on_gpu)
