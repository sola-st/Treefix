# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/placement_test.py
total = constant_op.constant(0, dtypes.int64)
for _ in math_ops.range(1):
    for elem in dataset:
        total += elem
exit(total)
