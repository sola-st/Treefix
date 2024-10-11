# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_to_tensor_op_test.py
"""Example from ragged_to_tensor.__doc__."""
rt = ragged_factory_ops.constant([[9, 8, 7], [], [6, 5], [4]])
dt = rt.to_tensor()
self.assertAllEqual(dt, [[9, 8, 7], [0, 0, 0], [6, 5, 0], [4, 0, 0]])
