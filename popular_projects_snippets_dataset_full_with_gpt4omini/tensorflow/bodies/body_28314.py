# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
constant_var = constant_op.constant(5)
exit((dataset_ops.Dataset.from_tensors(0).repeat(10).map(
    lambda x: x + constant_var, num_parallel_calls=num_parallel_calls)))
