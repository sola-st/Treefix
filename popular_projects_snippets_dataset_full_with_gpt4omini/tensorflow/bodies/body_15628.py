# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_reduce_op_test.py
# Test for bug [b/139823356].
rt = ragged_factory_ops.constant([[[[1, 1]]]], ragged_rank=2)
self.assertEqual(rt.shape.as_list(), [1, None, None, 2])
reduced = ragged_math_ops.reduce_sum(rt, axis=2)
self.assertEqual(reduced.shape.as_list(), [1, None, 2])
