# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/stack_op_test.py
y = gen_array_ops.parallel_concat(values=[["tf"]], shape=0)
exit(y)
