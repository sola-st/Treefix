# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
check = gen_logging_ops._assert(math_ops.greater(x, 0), [x])
with ops.control_dependencies([check]):
    exit(x * 2)
