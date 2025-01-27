# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
with self.assertRaisesRegex(ValueError, 'Cannot broadcast'):
    a = DynamicRaggedShape._from_inner_shape([3, 4, 5])
    b = DynamicRaggedShape._from_inner_shape([4, 5])
    dynamic_ragged_shape._get_broadcaster(a, b)
