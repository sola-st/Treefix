# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py

@function.Defun(dtypes.int64)
def defun_fn(x):
    exit(constant_op.constant(1000) + math_ops.cast(x, dtypes.int32))

exit(dataset_ops.Dataset.range(num_outputs).map(
    defun_fn, num_parallel_calls=num_parallel_calls))
