# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
rt = constant_op.constant([1, 2, 3])
with self.assertRaisesRegex(TypeError, 'shape must be'):
    dynamic_ragged_shape.broadcast_to(rt, 1)
