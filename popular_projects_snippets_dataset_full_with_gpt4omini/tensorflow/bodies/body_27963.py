# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/placement_test.py
value = constant_op.constant(0, dtype=dtypes.int64)
for d in iter(dataset_ops.Dataset.range(10)):
    value += d
exit(value)
