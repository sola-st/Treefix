# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_gather_nd_op_test.py
with self.assertRaisesRegex(error, message):
    ragged_gather_ops.gather_nd(params, indices)
