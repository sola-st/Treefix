# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/dynamic_stitch_op_test.py
indices = [
    constant_op.constant([0, 4, 7]),
    constant_op.constant([1, 6, 2, 3, 5])
]
data = [
    constant_op.constant([0, 40, 70]),
    constant_op.constant([[10, 60, 20, 30, 50]])
]
with self.assertRaises(ValueError):
    self.stitch_op(indices, data)
