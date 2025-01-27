# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_merge_dims_op_test.py
x = ragged_factory_ops.constant(rt, ragged_rank=ragged_rank)
with self.assertRaisesRegex(exception, message):
    self.evaluate(x.merge_dims(outer_axis, inner_axis))
