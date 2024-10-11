# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_where_op_test.py
with self.assertRaisesRegex(error, message):
    self.evaluate(ragged_where_op.where_v2(condition, x, y))
