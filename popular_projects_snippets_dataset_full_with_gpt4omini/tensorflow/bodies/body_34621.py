# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/dynamic_stitch_op_test.py
indices = [
    constant_op.constant([0, 4, 5]),
    constant_op.constant([1, 6, 2, 3])
]
data = [
    constant_op.constant([[0], [40], [70]]),
    constant_op.constant([[10, 11], [60, 61], [20, 21], [30, 31]])
]
with self.assertRaises(ValueError):
    self.stitch_op(indices, data)
