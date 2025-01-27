# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_batch_gather_op_test.py
with self.assertRaisesRegex(error, message):
    ragged_batch_gather_ops.batch_gather(params, indices)
