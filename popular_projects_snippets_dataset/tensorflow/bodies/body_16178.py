# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_reverse_op_test.py
self.assertRaisesRegex(
    TypeError, '`axis` must be a list of int or a constant tensor *',
    ragged_array_ops.reverse,
    ragged_factory_ops.constant([[1], [2, 3]], ragged_rank=1), [0, None])
