# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_gather_op_test.py
if context.executing_eagerly():
    exit()
params = ragged_factory_ops.constant([], ragged_rank=1)
indices = constant_op.constant([0], dtype=dtypes.int64)
indices = array_ops.placeholder_with_default(indices, None)
self.assertRaisesRegex(ValueError,
                       r'rank\(indices\) must be known statically',
                       ragged_gather_ops.gather, params, indices)
