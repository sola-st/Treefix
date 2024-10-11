# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
shape = DynamicRaggedShape.from_tensor(constant_op.constant([1, 2, 3]))
with self.assertRaisesRegex(TypeError, 'shape_y must be'):
    dynamic_ragged_shape.broadcast_dynamic_shape(shape, 1)
