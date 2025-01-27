# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_where_op_test.py
result = ragged_where_op.where_v2(condition, x, y)
self.assertAllEqual(result, expected)
