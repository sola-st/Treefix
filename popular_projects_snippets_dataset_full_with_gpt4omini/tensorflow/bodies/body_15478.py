# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_where_op_test.py
with self.assertRaisesRegex(error, message):
    ragged_where_op.where(condition, x, y)
