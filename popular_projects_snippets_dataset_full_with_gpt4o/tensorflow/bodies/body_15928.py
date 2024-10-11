# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
with self.assertRaisesRegex(ValueError,
                            'dtype must be tf.int32 or tf.int64'):
    DynamicRaggedShape.Spec._from_tensor_shape(
        [], tensor_shape.TensorShape([1, 2, 3]), dtypes.float32)
