# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_reduce_op_test.py
rt_input = ragged_factory_ops.constant(rt_input)
reduced = ragged_reduce_op(rt_input, axis, keepdims=keepdims)
self.assertAllEqual(reduced, expected)
